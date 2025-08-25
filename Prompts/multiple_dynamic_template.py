from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model="mistral")

"""chat_prompt = ChatPromptTemplate([
    SystemMessage(content="You are a {subject} teacher"),
    HumanMessage(content="Explain about the {topic}")
])"""

subject = input("What is the subject : ")
topic = input("What is the topic : ")

chat_temp = ChatPromptTemplate([
    ("system", "You are a {subject} teacher"),
    ("human", "Explain about the {topic}")
])

chat_prompt = chat_temp.invoke({
    "subject": subject,
    "topic": topic
})
result = model.invoke(chat_prompt)

print(AIMessage(content=result.content))

print("------------------------------------------")

print(chat_prompt)