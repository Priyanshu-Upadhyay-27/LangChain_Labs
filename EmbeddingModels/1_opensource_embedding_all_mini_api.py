from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from dotenv import load_dotenv
load_dotenv()


# Choose a supported embedding model (e.g., sentence-transformers)
model_name = "thenlper/gte-small"


# Initialize the embedding model
embedder = HuggingFaceInferenceAPIEmbeddings(
    model_name=model_name
)

# Embed a single sentence
query = "LangChain makes using LLMs easier."
embedding = embedder.embed_query(query)

print(f"Embedding length: {len(embedding)}")
print(embedding)


"""docs = ["LangChain is cool.", "Hugging Face provides many models."]
doc_embeddings = embedder.embed_documents(docs)"""

