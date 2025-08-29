from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int


def insert_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')


patient1={'name':'roshan','age':30}

patient=Patient(**patient1)

insert_data(patient)
