from typing import TypedDict#TypedDict is used to describe the expected structure of a dictionary.
class Person(TypedDict):
    name:str
    age:int 
new_person:Person={'name':'Ryan','age':98}# new_person is the new dictionary based on the structre defined by person
print(new_person)