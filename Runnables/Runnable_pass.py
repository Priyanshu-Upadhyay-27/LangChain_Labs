from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
# RunnablePassthrough is used to pass the input to the output as it is.

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt1 = PromptTemplate(
    template="Suggest a topic from Operating System for a Group Discussion in a tier 2 Indian College",
    input_variables=[]
)

prompt2 = PromptTemplate(
    template="Start the Group Discussion on the topic {text} by stating facts which supports the idea, you should be brief",
    input_variables=["text"]
)

parser = StrOutputParser()

chain0 = prompt1 | model | parser

chain1 = RunnableParallel({
    "top": RunnablePassthrough(),
    "exp": RunnableSequence(prompt2, model, parser)
})

final_chain = chain0 | chain1

result = final_chain.invoke({})

print(result)
