import chromadb


# Connect to ChromaDB client
client = chromadb.Client()


# Create a collection (you can name it as you wish)
collection = client.create_collection("my_collection")


# Add documents with unique ids (embeddings)
collection.add(
    documents=["Document 1", "Document 2"],
    metadatas=[{"key": "value"}, {"key": "value"}],
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],  # Example embeddings
    ids=["doc1", "doc2"]  # Unique ids for each document
)


# Fetch and print the stored docs
results = collection.get(ids=["doc1", "doc2"])
print(results)
