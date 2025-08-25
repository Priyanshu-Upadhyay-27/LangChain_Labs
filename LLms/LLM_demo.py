from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",
                             google_api_key = api_key)

result = llm.invoke("Who is the father of AI?")

print(result)