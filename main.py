from fastapi import FastAPI,Path,HTTPException,Query
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
    return {'Aight this company is cool...so do i think'}

#{patient_id} --> path parameter
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='patiend id in the DB',example='P001')):
    
    # load all the patient data 
    data=load_data()
    
    # checking if the patient_id exist in the data...if not return an error 
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail='Patient not found')
    
    
    # http://127.0.0.1:8000/sort?sort_by=height&order=desc
@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='Sort on the basis of height,weight or bmi'),
                  order:str=Query('asc',description='sort in ascending or descending order')):
    
    valid_fields={'height','weight','bmi'}
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'invalid field,select form {valid_fields}')

    if order not in {'asc','desc'}:
        raise HTTPException(status_code=400,detail='select between asc or desc')
    
    data=load_data()
        
    sort_order =  True if order=='desc' else False
    
    sorted_data = sorted(data.values(),key= lambda x:x.get(sort_by,0),reverse=sort_order)
    
    return sorted_data 
