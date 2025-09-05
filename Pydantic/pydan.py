from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Optional

class Patient(BaseModel):
    name:str='Anonymmous'
    email:EmailStr
    linkedin_profile_url:AnyUrl
    age:int
    weight:float
    allergies:Optional[List[str]] = None
    married:Optional[bool]=False
    

def insert_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_profile_url)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.allergies)
    print('inserted')
    
def udpate_data(patient:Patient):
    patient.name='rahul'
    print(patient.name)
    print(patient.age)
    print('updated')

patient1={'name':'roshan','age':30,'weight':61.3,'email':'roshan@gmail.com','linkedin_profile_url':'https://linkedin.com','allergies':['pollen','peanuts']}

patient=Patient(**patient1)

insert_data(patient)
udpate_data(patient)
