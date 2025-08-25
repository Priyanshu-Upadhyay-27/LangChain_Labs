from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

Llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-30B-A3B",
    task="text-generation",
    )

model = ChatHuggingFace(llm=Llm)

result = model.invoke("What is the capital of India?")

print(result.content)




"""from langchain_huggingface import HuggingFaceEndpoint  # ✅ NEW import
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

prompt = "What is the capital of India?"
result = llm.invoke(prompt)

print(result)"""
