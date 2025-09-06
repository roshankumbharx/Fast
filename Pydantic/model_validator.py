from pydantic import BaseModel, EmailStr,model_validator
from typing import List, Dict

# if we want to validate dependent field i.e data validation depending upon more than one field...then use @modelvalidator

# eg : if persons age>60 then the contact must have an emergency contact...if not then we wont allow

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'roshan', 'email':'roshan@hdfc.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462','emergency':'91991'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)