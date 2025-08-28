# It's a retriever that queries wikipedia api to fetch the relevant content for a given query.
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "The geopolitical history of India and Pakistan from the perspective of a chinese."

docs = retriever.invoke(query)
for i, doc in enumerate(docs):
    print(f"\n----{i+1}----")
    print(f"Content:\n {doc.page_content}....")

