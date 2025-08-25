from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template="Write an editorial for me, about {topic} being an editor at {editor} ",
    input_variables=["topic", "editor"]
)

parser = StrOutputParser()

chain0 = prompt1 | model | parser
chain1 = RunnableParallel({
    "editorial": RunnablePassthrough(),
    "count": RunnableLambda(word_count)
})

final_chain = chain0 | chain1

result = final_chain.invoke({"topic": "Donald Trump on India", "editor": "The Hindu Editor"})

final_result = """Editorial : \n {} \n word count - {}""".format(result["editorial"], result["count"])
print(final_result)
