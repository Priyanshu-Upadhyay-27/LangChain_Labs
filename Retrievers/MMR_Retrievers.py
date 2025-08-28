# It is a type of retriever which not only promises relevant results from the input documents, but also ensures that the
# results should be different or diversified and not redundant. As normal retrievers usually searches for semantic
# meaning and don't check the redundancy in the retriever whereas, MMR solves this problem.

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vector_store = Chroma(
    embedding_function=model,
    persist_directory="MyChromaDB",
    collection_name='sample'
)
vector_store.add_documents(docs)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.}
    # lambda_mult varies from 0-1 where 0 gives the most diversified content and 1 gives the redundant one.
)

query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


