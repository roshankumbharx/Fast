from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Patient(BaseModel):
    name:str
    city:str
    age:int
    gender:str
    height:float
    weight:float
    

@app.get('/home')
def hello():
    return {'message':'helloo there'}

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data
        