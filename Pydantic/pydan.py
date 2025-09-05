from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Optional,Annotated

# Field --> used for constraints 
# Annotated --> used to write metadata

class Patient(BaseModel):
    name:Annotated[str,Field(default='Anonymous',max_length=50,title='Name of the patient',description='Your Government Name',examples=['Roshan','Rahul'])]
    email:EmailStr
    linkedin_profile_url:AnyUrl
    age:int
    weight:Annotated[float,Field(gt=0,strict=True)]   # bcoz of 'strict' ab '61.3' allow nhi krega ...bas float allow krega
    allergies:Optional[List[str]] = Field(max_length=5)
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
