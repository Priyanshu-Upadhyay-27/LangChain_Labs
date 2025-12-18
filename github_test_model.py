from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    model="gpt-4o-mini"
)

response = llm.invoke("Give me 3 facts about APJ Abdul Kalam.")
print(response.content)