# 🧠 Vector Database Demo Collection

This repository contains Python demos for working with vector databases like ChromaDB, FAISS, Weaviate, Pinecone, and Neo4j — explored manually using VSCode. Some programs are adapted from the [vector-databases-course](https://github.com/pdichone/vector-databases-course), with a few customized extensions.

---

## 📦 Folder Structure

```
vector-db-demos/
├── chromadb/
│   ├── chroma_emb.py
│   ├── vector_db_llm.py
│   └── vector_db_llm_lang_chain.py
├── faiss/
│   ├── example.py
├── weaviate/
│   └── example.py
├── pinecone/
│   └── pinecone_db_llm_lang_chain.py
├── neo4j/
│   └── nexample.py
├── .env
├── .gitignore
└── requirements.txt
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/vector-db-demos.git
cd vector-db-demos
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (On Windows: venv\Scripts\activate)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
```bash
touch .env
```

Inside `.env`, add:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

---

## ▶️ How to Run Demos

### 🔹 ChromaDB
```bash
cd chromadb

#chromadb example
python chromadb_example.py

# similarity serach demos
python app.py         
python Text-similarity-search.py      # Custom semantic similarity demo    
python Doc-similarity-search.py         

# emb demos
python emb_example.py
python default_emb.py
python raw_emb.py
python openai_emb.py
python chroma_openai_emb.py


python chroma_persistent_openai.py     # Uses OpenAI embeddings with persistent Chroma

# vector db with llm (End-to-end example: Embed documents, store in ChromaDB, and query using semantic search with OpenAI.)
python vector_db_llm.py

# chromadb with langchain (# Full LangChain-based RAG pipeline using ChromaDB and OpenAI to retrieve and answer from document context.)
python vector_db_llm_langchain.py
```

### 🔹 FAISS
```bash
cd faiss
python faiss_intro.py                  # Intro to FAISS similarity search
python faiss_with_openai.py           # FAISS with OpenAI embeddings
```

### 🔹 Weaviate
```bash
cd weaviate
python weaviate_with_openai.py        # Semantic search with Weaviate + OpenAI
```

### 🔹 Pinecone
```bash
cd pinecone
python pinecone_db_llm_lang_chain.py              # Pinecone setup and query test
```

### 🔹 Neo4j
```bash
cd neo4j
python example.py          # Graph memory and context reasoning
```

---

## ✅ Notes

- All demos rely on `.env` for API keys (especially OpenAI)
- To change vector DBs, just switch folders and run relevant scripts
- Most demos use `langchain`, `chromadb`, or `sentence-transformers`

---

## 📚 Credits

Adapted from [`vector-databases-course`](https://github.com/pdichone/vector-databases-course)  
Customized and extended for hands-on LLM experiments
