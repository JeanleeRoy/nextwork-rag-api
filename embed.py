import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("k8s.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["k8s"])

print("Embedding stored in Chroma")


'''
✍️ What are embeddings and why did you create them?
Embeddings are.numerical representations of text that capture the semantic meaning of the content. I created them to enable efficient and accurate search and retrieval of information from my knowledge base using AI models.
The db/ folder contains the persistent storage for the Chroma database, which holds the embeddings and associated metadata. 
This is important for RAG because it allows the AI model to quickly access relevant information from the knowledge base when generating responses, improving the quality and relevance of the output.
'''
