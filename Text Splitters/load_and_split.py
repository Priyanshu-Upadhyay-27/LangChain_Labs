from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("Gradient Descent Research Paper.pdf")

docs = loader.load()

# print("Document list =", docs)
# print("Length of document =", len(docs))
#
# print("Type Of Documents =", type(docs))
#
# print("0th element as document object in list =", docs[0])
#
# print("Type of each element in document =", type(docs[0]))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=45,
    separator=''
)
result = splitter.split_documents(docs)
print("-------------------------------------------------------------")
print("Chunks =", result)


# template = PromptTemplate(
#     template="""Elaborate the project in detail by studying and analysing the {}""",
#     input_variables=["ppt"]
# )
# parser = StrOutputParser()
#
# chain = template | model | parser
#
# results = chain.invoke({'ppt': docs})
#
# print(results)