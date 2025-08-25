# Output Parser are used to convert LLMs responses to structured output .
# We will be using with String Output Parser, which takes the raw response of LLM and convert it into structured output.
# It is an alternative to result.content() .
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt1 = temp1.invoke(
    {
        "topic":top
    }
)

result1 = model.invoke(prompt1)

prompt2 = temp2.invoke(
    {
        "response":result1
    }
)

result2 = model.invoke(prompt2)

ans = result2.content

print(ans)