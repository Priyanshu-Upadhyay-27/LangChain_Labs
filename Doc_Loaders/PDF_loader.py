# It is used to read pdf files, which are simple and have computer like text and not scanned images. It works upon the
# Pypdf library. It works page by page, i.e. it makes the langchain document object for each page separately and return
# it as a list.
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("Swiggy-Revolutionizing-Food-Delivery.pdf")

docs = loader.load()

print("Document list =", docs)
print("Length of document =", len(docs))

print("Type Of Documents =", type(docs))

print("0th element in document =", docs[0])

print("Type of each element in document =", type(docs[0]))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

template = PromptTemplate(
    template="""Take Even Page no. slides from the {ppt} by reading the meta data and generate a short summary for each 
            one by reading the page_content""",
    input_variables=["ppt"]
)
parser = StrOutputParser()

chain = template | model | parser

results = chain.invoke({'ppt': docs})

print(results)

