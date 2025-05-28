import chromadb

from chromadb.utils import embedding_functions

# you can select bedrock, olllama, openai , other embedded functions
default_ef = embedding_functions.DefaultEmbeddingFunction() 

# Initialize persistent client and embedding function
chroma_client = chromadb.PersistentClient(path="./db/chromadb_store")

collection_name="my_story"

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(
    name=collection_name, 
    embedding_function=default_ef
)

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "Hello, how are you"},
    {"id": "doc3", "text": "Bye, world"},
    {
        "id": "doc4",
        "text": "Openai is an AI company"
    },
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=doc["text"])  

#define query
query = "Age of the Earth"

results = collection.query(
    query_texts=[query], # Chroma will embed this for you
    n_results=2 # how many results to return
)

#print(results)

for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance =  results["distances"][0][idx]
    print(
        f" For the query:{query}, \n Found similar document: {document} (ID: {doc_id}, Distance: {distance})"
    )