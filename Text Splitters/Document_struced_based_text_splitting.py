# It is similar to recursive based, but more, number of separators are used for different documents type like markdown
# code, or any other language code. It then divides according to these separators and then finally w.r.t para, line,
# word and character
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Calculator:
    def __init__(self, name="Simple Calculator"):
        self.name = name

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


calc = Calculator()

print(calc.name)                  
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
print("Division by zero:", calc.divide(10, 0))
"""

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=375,
    chunk_overlap=0
)

result = text_splitter.split_text(text)

print(result)
print("Length =", len(result))