from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str="nitish"
    email:EmailStr
    age:Optional[int]=None
    cpga:float=Field(gt=0,lt=10,default=5,description='it is a decimal value representing the cgpa of a student')# gt stands for greater than  . lt is less than

new_Student={'age':32,'email':'abc@gmail.com'}
student=Student(**new_Student)
print(student)
student_dict=dict(student)
json_student=student.model_dump_json()
print(json_student)


