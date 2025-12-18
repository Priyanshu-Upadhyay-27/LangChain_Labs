from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(template="Generate 5 interesting facts about the {topic}.",
                          input_variables=["topic"])

model = ChatOpenAI(model="gpt-4o-mini",
                   base_url="https://models.inference.ai.azure.com",
                   api_key=os.getenv("GITHUB_TOKEN"))

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "Elon Musk"})

print(result)

chain.get_graph().print_ascii()