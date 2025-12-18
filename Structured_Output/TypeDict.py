from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


newperson : Person = {"name": "Priyanshu", "age" : 20}

print(newperson)
print(type(newperson))
print(type(Person))