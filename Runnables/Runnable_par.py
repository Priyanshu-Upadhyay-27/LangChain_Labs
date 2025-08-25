from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

user_input = input("Enter the author name :")

prompt1 = PromptTemplate(
    template="Suggest a story or poem of author {per}",
    input_variables=["per"]
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Summarize the literature work {text}, using an paragraph tone",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Summarize the literature work {text}, using a poem tone",
    input_variables=["text"]
)
chain0 = prompt1 | model | parser
chain1 = RunnableParallel({
    "work":RunnableSequence( prompt2, model, parser),
    "sum":RunnableSequence(prompt3, model, parser),
})
final_chain = chain0 | chain1

result = final_chain.invoke({"per": user_input})
print(result["work"])
print("----------------")
print(result["sum"])