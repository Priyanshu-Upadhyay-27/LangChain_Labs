from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template1 = PromptTemplate(
    template="Assume yourself as a {persona} and Generate a detailed report on the {topic}",
    input_variable=["persona", "topic"]
)

template2= PromptTemplate(template="Generate a 5 point summary from the following text:\n{text}",
                          input_variable=["text"])

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({
    "persona" : "Field Reporter at The Hindu newspaper company",
    "topic": "Vijay Malya podcast with Raj Shamani"
})

print(result)

chain.get_graph().print_ascii()