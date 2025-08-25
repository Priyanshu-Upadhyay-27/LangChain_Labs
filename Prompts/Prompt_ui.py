from langchain_ollama import ChatOllama

model = ChatOllama(model="mistral")

prompt = "Summarize the research paper, Word2Vec"

result = model.invoke(prompt)

print(result)