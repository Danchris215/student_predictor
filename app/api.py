import numpy as np 
from fastapi import FastAPI 
from pydantic import BaseModel 
from src.config import MODEL_PATH
import pickle 

app = FastAPI()

@app.get("/")
def home():
    return{
        "message": "Student Predictor Model"
    }

#we define the schema(what we expect) which aids validation 
class Student(BaseModel):
    hours_studied: float
    attendance: float 
    previous_gpa: float 

#load the model 
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

mean = model["mean"]
std = model["std"]

@app.post("/predict")
def predict(student: Student):
    x = np.array([[
        student.hours_studied,
        student.attendance,
        student.previous_gpa
    ]])

    x = (x - mean)/std
    x = np.hstack([np.ones((x.shape[0], 1)), x]) 

    weights = model["weights"]

    z = x @ weights 
    prob = 1/(1+np.exp(-z))
    pass_prob = float(prob.item())
    
    y_pred = (prob >= 0.5).astype(int).item()
    return{
        "Prediction": y_pred,
        "Pass_Probability": pass_prob
    }

