from pydantic import BaseModel


class Address(BaseModel):
    city:str
    state:str
    pin_code:str
        
        
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
        

def update_details(patient:Patient):
    print(patient.name)
    print(patient.gender)
    print(patient.age)
    print(patient.address)
    print(patient.address.city)


address_dict={'city':'Mumbai','state':'Maharahstra','pin_code':'400090'}
address1=Address(**address_dict)


patient_info={'name':'roshan','gender':'male','age':30,'address':address1}

patient1=Patient(**patient_info)

update_details(patient1)