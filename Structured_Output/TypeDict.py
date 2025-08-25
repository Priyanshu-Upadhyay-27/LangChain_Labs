from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


newperson : Person = {"Name": "Priyanshu", "Age" : "20"}

print(newperson)
