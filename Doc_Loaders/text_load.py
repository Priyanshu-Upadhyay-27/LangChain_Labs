# take text file and convert it into common document object
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

template = PromptTemplate(
    template="Summarize the document provided: \n {doc}",
    input_variables=["doc"]
)

parser = StrOutputParser()

loader = TextLoader("Poem.txt", encoding="utf-8") # object

docs = loader.load() # docs will be a list of document object

print(type(docs[0]))

print(len(docs))

chain = template | model | parser

result = chain.invoke({"doc": docs[0].page_content})
print(result)


