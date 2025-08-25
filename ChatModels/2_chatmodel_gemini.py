from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=1, max_completion=5)

result = model.invoke("Write a short poem about the topic, 'Love' ")

print(result)