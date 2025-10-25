from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
import json
from typing import Annotated,Literal

app = FastAPI()


class Patient(BaseModel):
    id:Annotated[str,Field(...,description='Id of the patient',examples=['P001','P002'])]
    name:Annotated[str,Field(default='Anonymous',title='Name of the Patient',desc = 'Patients Government Name',examples=['Sherlock','Moriarty'])]
    city:Annotated[str,Field(...,description='City of Patient',examples=['New York','London'])]
    age:Annotated[int,Field(...,gt=0,lt=200,description='Age of patient')]
    gender:Annotated[Literal['male','female','others    '],Field(...,description='Gender of the Patient')]
    height:Annotated[float,Field(...,gt=0,description='Height of the patient in metres')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round((self.weight)/(self.height**2),2)
        return bmi
        
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'Underweigth'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

@app.get('/home')
def hello():
    return {'message':'helloo there'}

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data
    
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)   


@app.post('/create')
def create_patient(patient:Patient):
    
    # load existing data
    data = load_data()
    
    # check if patient already exist
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')  
    
    # add new patient to databsase
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    save_data(data)
    
    return JSONResponse(status_code=200,content={'message':'Patient created succesfully'})