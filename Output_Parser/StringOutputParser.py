from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser #1

"""
It returns the raw LLM output as a clean string.

Removes extra whitespace, but does NOT enforce structure.

Use it when you don’t need formatting—just take whatever the LLM writes.
"""

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-30B-A3B",
    task="text-generation",
)

model1 = ChatHuggingFace(llm=llm)
model2 = ChatGroq(model_name="llama-3.3-70b-versatile")

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

chain = temp1 | model2 | parser| temp2 | model2 | parser # Chains

response = chain.invoke({"topic":top})

print(response)