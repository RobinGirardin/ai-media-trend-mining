> [!WARNING]
> This `README.md` is at the boilerplate stage and do not represent faithfully the repository's content and purpose.

# AI Media Trend Mining

NLP-driven analysis of AI media to track trends, extract knowledge, and build RAG-based Q&A systems.

---

## 📌 Project Overview

This repository contains the implementation of a three-stage NLP pipeline designed to analyze large-scale AI media discourse. The project focuses on uncovering emerging AI trends, mapping innovations, and building knowledge-aware question answering systems using modern NLP and language models.

The work is based on a curated AI media dataset (Sept 2024 – Sept 2025) and is developed as part of a graduate-level project in Computational Language Technologies.

---

## 🎯 Objectives

- Analyze AI-related media coverage to identify trends and sentiment over time  
- Extract entities and relations to construct a knowledge graph of the AI ecosystem  
- Train and evaluate classical and modern embedding models on domain-specific text  
- Build a Retrieval-Augmented Generation (RAG) system for AI trend–focused Q&A  

---

## 🧩 Project Structure

The project is organized into three main stages:

### **Stage 1: Data Cleaning & Exploratory Analysis**
- Data cleaning and normalization
- Text preprocessing (tokenization, lemmatization, stopword removal)
- Temporal and sentiment analysis
- Topic modeling (e.g. LDA, BERTopic)
- Entity & relation extraction
- Knowledge graph construction and visualization

📂 Output:
- Preprocessing and EDA notebooks  
- Visualizations of trends and sentiment  
- Initial knowledge graph  

---

### **Stage 2: Embedding Models & Representation Learning**
- Training classical embeddings (Word2Vec, FastText, Doc2Vec)
- Fine-tuning compact open-source language models
- Intrinsic and extrinsic evaluation of embeddings
- Comparative analysis of model performance and efficiency

📂 Output:
- Model training and evaluation notebooks  
- Embedding visualizations and comparisons  
- Summary of insights on trend detection  

---

### **Stage 3: RAG-Based Question Answering**
- Construction of a Q&A benchmark
- Integration of text retrieval with a knowledge graph
- Implementation of a RAG pipeline
- Evaluation of faithfulness, relevance, and grounding
- Comparison of text-only vs graph-augmented RAG

📂 Output:
- End-to-end RAG notebook  
- Evaluation tables and visualizations  
- (Optional) enhancement proposal  

---

## 📁 Repository Layout (Planned)

```text
ai-media-trend-mining/
│
├── data/                 # Dataset samples or data loaders (if permitted)
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_embeddings.ipynb
│   └── 03_rag.ipynb
├── src/                  # Reusable code (preprocessing, models, utils)
├── tests/                # Tests for reusable code
├── requirements.txt
└── README.md

```

## Neo4j - Graph Database

For this project's graph database, we'll use Neo4j, a common industry solution when deploying graph database architecture.
For this project, we'll use the free tier of Neo4j Aura, a managed cloud infrastructure.

To connect and interact with the graph database instance, you'll need the following username and password.

* Username: 88ad2b04
* Password: sSGPYB5Zmtsnu0wNu0JoCmH2gjC2OTNOcoF2ffr7WHs
* Connection URI: neo4j+s://88ad2b04.databases.neo4j.io
* Connection URL: https://88ad2b04.databases.neo4j.io

The simplest way to interact with the database, is trough the browser.
Use the *Connection URL* in the browser, connect using the previously mentioned credentials and start querying.

> [!NOTE]:
> **Note** the difference between URL and URI connection string.
To connect through the browser, use the URL connection string.
For python, use the URI connection string.


Alternatively, you can do this programmatically through `neo4j` python library and the **Connection URI** string.

```python
from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "<database-uri>"
AUTH = ("<username>", "<password>")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
```
