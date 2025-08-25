from pydantic import BaseModel, EmailStr, Field
from typing import Optional


#In the dictionary below, default value can be given and later can be skipped in the new dictionary
class student(BaseModel):

    name: str = "Priyanshu"
    age: Optional[int] = None # optional value is used to send any optional parameter
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description="Decimal value representing the cgpa of the student")

new_student = {"age": "20", "email" : "priyanshucodes27@gmail.com", "cgpa" : 9}
#here pydantic is smart enough to understand that user has given 20 in string format, so it,
#Implicitly convert that string format 20 to integer format 20

student1 = student(**new_student)

student1_dict = dict(student1)

student1_json = student1.json()

print(student)
print(student1)
print(type(student1))
print(student1_dict["age"])
print(student1_json)
