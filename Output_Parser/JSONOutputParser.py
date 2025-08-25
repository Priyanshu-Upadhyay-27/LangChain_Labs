from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser #2


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

parser = JsonOutputParser()

temp = PromptTemplate(template="Give me a name, age, city of a fictional person \n {format_instruction}",
                      input_variables=[],
                      partial_variables={"format_instruction":parser.get_format_instructions()},
)
prompt = temp.format()

result = model.invoke(prompt)

final_parsed_result = parser.parse(result.content)
print(final_parsed_result)