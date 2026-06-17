from pydantic import BaseModel
class Student(BaseModel):
    name:str='Nitish'

#new_student={'name':32}#this gives a error as name should always be a string
new_student={}
student=Student(**new_student)
print(student.name)