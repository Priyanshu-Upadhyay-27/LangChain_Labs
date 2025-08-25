from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser #1

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-30B-A3B",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

top = input("Enter the topic : ")

temp1 = PromptTemplate(
    template="Generate a detailed report on the topic: {topic}",
    input_variables=["topic"]
)

temp2 = PromptTemplate(
    template="Generate a 5 line summary on the text report \n  {response}",
    input_variables=["response"]
)

parser = StrOutputParser()

chain = temp1 | model | parser| temp2 | model | parser # Chains

response = chain.invoke({"topic":top})

print(response)