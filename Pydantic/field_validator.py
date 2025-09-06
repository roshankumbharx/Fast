from pydantic import BaseModel, EmailStr, AnyUrl, Field,field_validator
from typing import List, Dict, Optional, Annotated

# field validtor is used for custom data validation  but only works for a single field 
# if we want to validate dependent field ...then use @modelvalidator

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains={'hdfc.com','icici.com'}
        # 'roshan@gmail.com'
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_to_uppercase(cls,value):
        return value.upper()
    
    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls, value):
        if 18<value<60:
            return value
        else:
            raise ValueError('Age must be between 18 and 60')
        
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'roshan', 'email':'roshan@hdfc.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)