from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema #3

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

schema = [
    ResponseSchema(name="Fact1", description="Fact 1 about the topic"),
    ResponseSchema(name="Fact2", description="Fact 2 about the topic"),
    ResponseSchema(name="Fact3", description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

temp = PromptTemplate(
    template="Give 3 facts about the {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = temp.invoke({"topic": "Worm Holes"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)
