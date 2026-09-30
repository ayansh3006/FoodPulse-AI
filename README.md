# 🍽️ FoodPulse AI

> An end-to-end AI-powered food analytics platform combining Data Engineering, Cloud Data Warehousing, Business Intelligence, Generative AI, RAG, and Natural Language-to-SQL.

FoodPulse AI transforms raw food-ordering data into structured analytical datasets and AI-powered applications that allow users to explore business metrics and customer feedback using natural language.

---

## 🚀 Project Overview

FoodPulse AI is a complete Data Engineering + Generative AI project built around a modern analytics architecture.

The platform takes raw food-ordering datasets, loads them into Snowflake, transforms them using dbt, orchestrates the pipeline with Apache Airflow, enriches customer reviews using LLMs, and exposes the resulting data through AI-powered Streamlit applications.

### End-to-End Pipeline

    Raw CSV Data
          │
          ▼
    ┌──────────────────┐
    │     Snowflake    │
    │    RAW Layer     │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │       dbt        │
    │ Staging + Marts  │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │     Airflow      │
    │  Orchestration   │
    └────────┬─────────┘
             │
        ┌────┴────┐
        ▼         ▼
    AI Review   Business
    Enrichment  Analytics
        │         │
        ▼         ▼
    RAG Chatbot  Text-to-SQL


---

## 🧰 Complete Tech Stack

### ☁️ Cloud & Data Warehouse

- Snowflake
- Snowflake SQL
- Snowflake Stages
- Snowflake Warehouses
- Snowflake Roles
- Snowflake Schemas

### 🔄 Data Engineering

- dbt
- SQL
- ELT
- Data Modeling
- Dimensional Modeling
- Fact Tables
- Dimension Tables
- Staging Models
- Analytical Data Marts
- dbt Sources
- dbt Tests
- dbt Macros

### ⚙️ Workflow Orchestration

- Apache Airflow
- Airflow DAGs
- Scheduled Batch Pipelines
- SQLExecuteQueryOperator
- BashOperator
- Task Dependencies

### 🐳 Containerization

- Docker
- Docker Compose
- Custom Airflow Dockerfile
- Containerized Development Environment

### 🐍 Programming

- Python
- Pandas
- NumPy
- JSON
- Python Virtual Environment

### 🤖 Generative AI

- OpenRouter
- Large Language Models (LLMs)
- Prompt Engineering
- Structured JSON Generation
- LLM-based Text Classification
- Natural Language Processing

### 🧠 AI / Machine Learning

- Sentence Transformers
- all-MiniLM-L6-v2
- Text Embeddings
- Semantic Search
- Vector Similarity
- Retrieval-Augmented Generation (RAG)

### 💬 AI Applications

- Streamlit
- RAG Chatbot
- Text-to-SQL
- Natural Language Data Exploration

### 📊 Analytics

- SQL
- Snowflake SQL
- Business Intelligence
- KPI Analysis
- Revenue Analysis
- Restaurant Performance
- Delivery SLA Analysis
- Customer Review Analysis

### 🔧 Development Tools

- Git
- GitHub
- VS Code
- PowerShell


---

## 🏗️ System Architecture

    FOODPULSE AI
          │
          ▼
    ┌───────────────────┐
    │   Raw CSV Data    │
    └─────────┬─────────┘
              │
              ▼
    ┌───────────────────┐
    │     Snowflake     │
    │    RAW Schema     │
    └─────────┬─────────┘
              │
              ▼
    ┌───────────────────┐
    │       dbt         │
    │                   │
    │ Staging Models    │
    │       ↓           │
    │ Dimensions        │
    │       ↓           │
    │ Facts + Marts     │
    └─────────┬─────────┘
              │
              ▼
    ┌───────────────────┐
    │      Airflow      │
    │ Batch Orchestration│
    └─────────┬─────────┘
              │
        ┌─────┴─────┐
        │           │
        ▼           ▼
    AI Review    Business
    Enrichment   Analytics
        │           │
        ▼           ▼
    REVIEW_       Analytical
    ENRICHED      Marts
        │           │
        ▼           ▼
    RAG Chatbot   Text-to-SQL


---

## ❄️ Snowflake Architecture

Snowflake acts as the central data warehouse.

    FOODPULSE
    │
    ├── RAW
    │   ├── RESTAURANTS
    │   ├── USERS
    │   ├── FOOD
    │   ├── MENU
    │   ├── ORDERS
    │   ├── ORDER_ITEMS
    │   └── REVIEWS
    │
    ├── STAGING
    │   ├── STG_RESTAURANTS
    │   ├── STG_USERS
    │   ├── STG_FOOD
    │   ├── STG_MENU
    │   ├── STG_ORDERS
    │   ├── STG_ORDER_ITEMS
    │   └── STG_REVIEWS
    │
    ├── MARTS
    │   ├── DIM_CUSTOMER
    │   ├── DIM_DATE
    │   ├── DIM_FOOD
    │   ├── DIM_RESTAURANTS
    │   ├── FCT_ORDERS
    │   ├── FCT_ORDER_ITEMS
    │   ├── MART_DAILY_CITY_REVENUE
    │   ├── MART_DELIVERY_SLA
    │   └── MART_RESTAURANT_PERFORMANCE
    │
    └── AI
        └── REVIEW_ENRICHED


---

## 🔄 Data Engineering Pipeline

The data pipeline follows a structured ELT architecture.

### 1. Raw Data

Raw CSV datasets contain information about:

- Restaurants
- Users
- Food
- Menu
- Orders
- Order Items
- Reviews

The raw data is loaded into the Snowflake RAW schema.

### 2. Staging

dbt staging models clean and standardize the raw data.

- STG_RESTAURANTS
- STG_USERS
- STG_FOOD
- STG_MENU
- STG_ORDERS
- STG_ORDER_ITEMS
- STG_REVIEWS

### 3. Data Modeling

The transformed data is organized into dimensions, facts, and analytical marts.

#### Dimensions

- DIM_CUSTOMER
- DIM_DATE
- DIM_FOOD
- DIM_RESTAURANTS

#### Facts

- FCT_ORDERS
- FCT_ORDER_ITEMS

#### Analytical Marts

- MART_DAILY_CITY_REVENUE
- MART_DELIVERY_SLA
- MART_RESTAURANT_PERFORMANCE
- MARTS_REVIEW_INSIGHTS


---

## 🤖 AI Review Enrichment

FoodPulse AI uses an LLM to transform unstructured customer reviews into structured analytical information.

### Input

Customer Review

### LLM Processing

The model analyzes each review and generates:

- Sentiment Label
- Sentiment Score
- Topic
- Key Issue

### Example

Review:

"Food was good but delivery was extremely late."

AI Enrichment:

- Sentiment: Negative
- Topic: Delivery
- Sentiment Score: -0.7
- Key Issue: Late delivery

The resulting structured data is stored in:

FOODPULSE.AI.REVIEW_ENRICHED


---

## 🧠 Retrieval-Augmented Generation (RAG)

FoodPulse AI includes a RAG-powered customer review chatbot.

The application combines:

- Snowflake review data
- Sentence Transformer embeddings
- Semantic similarity search
- OpenRouter LLM
- Streamlit

### RAG Pipeline

    User Question
          ↓
    Sentence Transformer
          ↓
    Query Embedding
          ↓
    Semantic Similarity Search
          ↓
    Top Relevant Reviews
          ↓
    LLM Context
          ↓
    Generated Answer

### Example Question

"What are the most common complaints about delivery?"

The application retrieves the most relevant reviews and generates an answer based on the retrieved context.


---

## 💬 Text-to-SQL Application

FoodPulse AI provides a natural-language interface for querying analytical data.

### Workflow

    Natural Language Question
              ↓
             LLM
              ↓
         SQL Generation
              ↓
         SQL Validation
              ↓
           Snowflake
              ↓
          Query Result
              ↓
          Streamlit UI

### Example

"Which cities generated the highest revenue?"

The application generates an analytical SQL query, executes it against Snowflake, and displays the result.

### Security

The application restricts SQL execution to read-only queries and blocks potentially destructive SQL operations.


---

## ⚙️ Apache Airflow

Airflow orchestrates the complete batch workflow.

### DAG

    reload_raw
         ↓
    dbt_build_core
         ↓
    enrich_reviews
         ↓
    dbt_build_ai

### Pipeline Responsibilities

#### reload_raw

Loads raw data into Snowflake.

#### dbt_build_core

Builds staging and analytical models.

#### enrich_reviews

Uses an LLM to enrich customer reviews.

#### dbt_build_ai

Builds AI-related dbt models.


---

## 📊 Analytical Use Cases

FoodPulse AI enables analysis of:

### Revenue

- Daily revenue
- City-level revenue
- Restaurant revenue
- Revenue trends

### Restaurants

- Restaurant performance
- Restaurant ratings
- Customer feedback
- Restaurant-level KPIs

### Customers

- Customer activity
- Order behavior
- Review behavior

### Delivery

- Delivery performance
- Delivery SLA
- Late deliveries

### Reviews

- Customer sentiment
- Review topics
- Key customer issues
- Common complaints


---

## 📂 Project Structure

    FoodPulse AI/
    │
    ├── ai/
    │   ├── enrich_reviews.py
    │   ├── rag_chat.py
    │   └── text_to_sql.py
    │
    ├── airflow/
    │   ├── dags/
    │   │   └── foodpulse_batch.py
    │   ├── Dockerfile
    │   └── docker_compose.yml
    │
    ├── foodpulse/
    │   ├── analyses/
    │   ├── macros/
    │   ├── models/
    │   │   ├── marts/
    │   │   └── staging/
    │   ├── seeds/
    │   ├── snapshots/
    │   ├── tests/
    │   ├── dbt_project.yml
    │   └── profiles.yml
    │
    ├── Data/
    │   └── Raw datasets
    │
    ├── .gitignore
    └── README.md


---

## 🧠 AI Module

The AI layer contains three major components:

### enrich_reviews.py

Performs LLM-based customer review enrichment.

### rag_chat.py

Provides the customer review RAG chatbot.

### text_to_sql.py

Provides the natural-language-to-SQL application.


---

## 🗃️ dbt Layer

The dbt layer handles:

- Data transformation
- Data modeling
- Source definitions
- Analytical marts
- AI models
- SQL transformations
- Reusable macros
- Data quality testing


---

## 🐳 Docker

Docker is used to provide a reproducible environment for Airflow.

The project includes:

- Dockerfile
- Docker Compose configuration

Docker Compose manages the Airflow-related services required for orchestration.


---

## 🖥️ Streamlit Applications

FoodPulse AI contains two interactive applications.

### Review RAG Chatbot

File:

ai/rag_chat.py

Used for natural-language exploration of customer reviews.

### Text-to-SQL

File:

ai/text_to_sql.py

Used for natural-language exploration of business analytics data.


---

## 🔐 Security & Secrets

Sensitive information is not stored in the repository.

The project uses environment variables for credentials such as:

- SNOWFLAKE_ACCOUNT
- SNOWFLAKE_USER
- SNOWFLAKE_PASSWORD
- OPENROUTER_API_KEY

The .gitignore configuration excludes:

- .env files
- API keys
- Credentials
- Large datasets
- Python cache
- Airflow logs
- dbt generated files
- RAG embedding cache
- IDE files

> Never commit secrets, API keys, passwords, or credentials to GitHub.


---

## 📦 Dataset

The raw datasets are intentionally excluded from this repository because of their large file sizes.

The project uses datasets related to:

- Restaurants
- Users
- Food
- Menu
- Orders
- Order Items
- Reviews

The datasets should be loaded into the Snowflake RAW layer before executing the complete pipeline.


---

## ▶️ Getting Started

### 1. Clone the Repository

    git clone https://github.com/ayansh3006/FoodPulse-AI.git
    cd FoodPulse-AI

### 2. Configure Environment Variables

Create your local environment configuration containing the required Snowflake and OpenRouter credentials.

Do not commit this file.

### 3. Start Airflow

    cd airflow
    docker compose -f docker_compose.yml up -d

Airflow UI:

http://localhost:8080

### 4. Run the RAG Application

    cd ai
    streamlit run rag_chat.py

### 5. Run the Text-to-SQL Application

    streamlit run text_to_sql.py


---

## 🧪 Data Quality & Validation

The project uses dbt's modeling and testing capabilities to help validate the analytical data layer.

Validation includes:

- Source configuration
- Model dependencies
- SQL transformations
- Data relationships
- Analytical model construction


---

## 📈 Key Project Highlights

- Built an end-to-end Data Engineering + GenAI platform
- Implemented Snowflake data warehouse architecture
- Developed transformation pipelines using dbt
- Built analytical fact and dimension models
- Created business-focused analytical data marts
- Orchestrated workflows using Apache Airflow
- Containerized Airflow using Docker
- Implemented LLM-based customer review enrichment
- Built a Retrieval-Augmented Generation chatbot
- Implemented semantic search using Sentence Transformers
- Built a Natural Language-to-SQL application
- Added SQL safety validation for generated queries
- Developed interactive applications using Streamlit
- Managed project version control using Git and GitHub


---

## 🎯 Skills Demonstrated

- Data Engineering
- SQL
- Python
- Snowflake
- dbt
- Apache Airflow
- Docker
- Data Warehousing
- Dimensional Modeling
- ETL / ELT
- Data Analytics
- Generative AI
- LLMs
- Prompt Engineering
- RAG
- Semantic Search
- Text Embeddings
- Text-to-SQL
- Streamlit
- Git
- GitHub


---

## 🔮 Future Improvements

Potential extensions include:

- Power BI dashboard integration
- Automated data quality monitoring
- Advanced review analytics
- Real-time data ingestion
- Vector database integration
- Advanced recommendation systems
- Automated model evaluation
- Cloud deployment
- CI/CD pipeline
- Monitoring and observability


---

## 👨‍💻 Author

### Ayansh Singh

B.Tech — Computer Science & Engineering

Specialization: Data Science & AI

GitHub:

https://github.com/ayansh3006


---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.