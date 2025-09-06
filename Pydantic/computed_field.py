from pydantic import BaseModel,EmailStr,computed_field
from typing import Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    height:float
    weight:float
    contact:Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round((self.weight)/(self.height**2),2)
        return bmi

def insert_data(patient:Patient):
    print(patient.name)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    print('inserted')

patient_info = {'name':'roshan','email':'roshan@gmail.com','age':30,'height':1.72,'weight':59.3,'contact':{'ph_no':'91999'}}    
paitent1=Patient(**patient_info)

insert_data(paitent1)