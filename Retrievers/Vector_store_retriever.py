# It is a type of Retriever that let's you search and fetch documents from a vector store based on semantic similarity.
#using vector embeddings.

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

docs =[
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models.")
]

embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embed_model,
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "What are embeddings?"
results = retriever.invoke(query) # .search_query() can be used too.
print(results)

for i, doc in enumerate(results):
    print(f"/n-----{i+1}-----")
    print(doc.page_content)



