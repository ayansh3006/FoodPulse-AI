import os
import numpy as np
import pandas as pd
import streamlit as st
import snowflake.connector
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

CHAT_MODEL = "openrouter/free"

NEW_REVIEWS = 500
TOP_K = 5
CACHE_FILE = "review_embeddings.parquet"

# Local embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# ============================================================
# OPENROUTER CLIENT
# ============================================================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# ============================================================
# LOCAL EMBEDDING MODEL
# ============================================================

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)


embedding_model = load_embedding_model()


# ============================================================
# READ REVIEWS FROM SNOWFLAKE
# ============================================================

def read_reviews_from_snowflake():

    conn = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

    query = f"""
        SELECT
            REVIEW_ID,
            CITY,
            RATING,
            COMMENT
        FROM FOODPULSE.STAGING.STG_REVIEWS
        SAMPLE ({NEW_REVIEWS} ROWS)
    """

    cursor = conn.cursor()

    try:
        df = cursor.execute(query).fetch_pandas_all()
    finally:
        cursor.close()
        conn.close()

    df.columns = [col.lower() for col in df.columns]

    return df


# ============================================================
# CREATE LOCAL EMBEDDINGS
# ============================================================

def embed(texts):

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings.tolist()


# ============================================================
# LOAD REVIEWS
# ============================================================

@st.cache_data
def load_reviews():

    if os.path.exists(CACHE_FILE):

        return pd.read_parquet(CACHE_FILE)

    df = read_reviews_from_snowflake()

    # Remove rows where comment is missing
    df = df.dropna(subset=["comment"]).copy()

    df["embedding"] = embed(
        df["comment"].tolist()
    )

    df.to_parquet(CACHE_FILE)

    return df


# ============================================================
# STREAMLIT UI
# ============================================================

st.title("Chat with your FoodPulse Reviews")

st.caption(
    f"Searching {NEW_REVIEWS} reviews using local embeddings "
    f"and answering with {CHAT_MODEL}"
)


# ============================================================
# COSINE SIMILARITY
# ============================================================

def cosine_similarity(vec_a, vec_b):

    return np.dot(vec_a, vec_b) / (
        np.linalg.norm(vec_a) *
        np.linalg.norm(vec_b)
    )


# ============================================================
# FIND SIMILAR REVIEWS
# ============================================================

def find_similar_reviews(question, df):

    question_vector = embed([question])[0]

    scores = []

    for review_vector in df["embedding"]:

        scores.append(
            cosine_similarity(
                question_vector,
                review_vector
            )
        )

    df = df.copy()

    df["score"] = scores

    return df.nlargest(TOP_K, "score")


# ============================================================
# ASK OPENROUTER
# ============================================================

def ask_llm(question, top_reviews):

    context = ""

    for _, row in top_reviews.iterrows():

        context += (
            f"({row['city']}, {row['rating']} stars) "
            f"{row['comment']}\n"
        )

    system_prompt = (
        "You are the FoodPulse AI review assistant. "
        "Answer ONLY using the customer reviews provided. "
        "Be concise. "
        "If the provided reviews do not cover the question, "
        "say so clearly."
    )

    user_prompt = (
        f"Question: {question}\n\n"
        f"Reviews:\n{context}"
    )

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    if not answer:
        return "The AI returned an empty response. Please try again."

    return answer


# ============================================================
# LOAD DATA
# ============================================================

review_df = load_reviews()


# ============================================================
# QUESTION INPUT
# ============================================================

question = st.text_input(
    "Ask a question about your FoodPulse reviews:",
    placeholder=(
        "e.g. What are the most common complaints "
        "about delivery?"
    )
)


# ============================================================
# GENERATE ANSWER
# ============================================================

if question:

    top_reviews = find_similar_reviews(
        question,
        review_df
    )

    answer = ask_llm(
        question,
        top_reviews
    )

    st.markdown("### Answer")

    st.write(answer)

    with st.expander(
        "Reviews used to build this answer"
    ):

        st.dataframe(
            top_reviews[
                ["city", "rating", "comment"]
            ],
            hide_index=True
        )