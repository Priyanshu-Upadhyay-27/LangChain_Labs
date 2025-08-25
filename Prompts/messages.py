from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

messages = [
    SystemMessage(content="You are a great Engineer"),
    HumanMessage(content="Tell me about Mechatronics")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

