# PydanticOutputParser is a structured output parser in LangChain that uses Pydantic models to enforce \
# schema validation when processing LLM responses.

# Why Use PydanticOutputParser ?
# Strict Schema Enforcement - Ensures that LLM responses follow a well-defined structure.
# Type Safety - Automatically converts LLM outputs into Python objects.
# Easy Validation - Uses Pydantic's built-in validation to catch incorrect or missing data.
# Seamless Integration - Works well with other LangChain components.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser #4
from pydantic import BaseModel, Field


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

class Adult(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age pf the Person")
    city: str = Field( description="City of the person from where he belongs")

parser = PydanticOutputParser(pydantic_object = Adult)

temp = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt = temp.invoke({"place":"Indian"})
print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)