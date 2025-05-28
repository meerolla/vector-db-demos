import chromadb
chroma_client = chromadb.Client()

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "Hello, how are you"},
    {"id": "doc3", "text": "Bye, world"},
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=doc["text"])  

#define query
query = "Hello, world!"

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