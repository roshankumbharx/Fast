from fastapi import FastAPI
import json

app=FastAPI()

@app.get('/')
def hello():
    return {'message':'Hello World!'}

def load_data():
    with open ('patients.json','r') as f:
        data=json.load(f)
        
    return data
    

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/about')
def about():
    return {'Aight this company is cool af...so do i think'}

@app.post('/about')
def type():
    pass
