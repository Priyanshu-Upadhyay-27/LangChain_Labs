from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model1 = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-lite")

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(description = "Classify the sentiment based on the text provided")

parser2 = PydanticOutputParser(pydantic_object = Feedback)
template1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text provided into positive, negative or neutral\n{feedback}\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser2.get_format_instructions()
    }
)

classifier_chain = template1 | model1 | parser2

"""result = classifier_chain.invoke({
    "feedback": "I had brought a Samsung curve screen tv 1 year ago and it is not good or bad"
})"""

prompt2 = PromptTemplate(
    template="Write a **single, short, professional** response to this positive feedback : \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write a **single, short, professional** response to this negative feedback : \n {feedback}",
    input_variables=["feedback"]
)

prompt4 = PromptTemplate(
    template="Write a **single, short, professional** response to this neutral feedback : \n {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model1 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model1 | parser),
    (lambda x: x.sentiment == "neutral", prompt4 | model1 | parser),
    RunnableLambda(lambda x: "couldn't find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({
    "feedback":"This is the new Samsung S25 Ultra and it's just a copy of previous model with only a few new feature "
})

print(result)

chain.get_graph().print_ascii()


