from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))  # total 1000 pages

print(docs[50].page_content)
print(docs[50].metadata)