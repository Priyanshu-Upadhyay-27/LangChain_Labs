from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

user_input = input("Enter the genre :")

prompt1 = PromptTemplate(
    template="""Suggest a single Movie or a web series which I can watch and which
             belongs to the {genre} genre""",
    input_variables=["genre"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Tell me about the {title} in 5 points",
    # Catch: Here when the chain saw, the string output is coming
    # from the parser, then 2nd PromptTemplate wants to input the custom variable you have set, and the data type remains
    # string only, but when we use text as variable, langchain automatically map the string input of the parser into a
    # dictionary and expected input for second prompt can be made.
    input_variables=["title"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"genre": user_input})

print(result)