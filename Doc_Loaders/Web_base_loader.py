from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

template = PromptTemplate(
    template="Summarize the page content and tell what is the topic of discussion in: \n {doc}",
    input_variables=["doc"]
)

parser = StrOutputParser()

url="https://medium.com/@narwar_veer/slices-in-golang-0afebbf41133"
loader = WebBaseLoader(url)

scrap = loader.load()
print(type(scrap))
print(scrap[0].page_content)
print(scrap[0].metadata)

print("--------------------------------")

chain = template | model | parser
result = chain.invoke({
    "doc": scrap[0].page_content
})

print(result)