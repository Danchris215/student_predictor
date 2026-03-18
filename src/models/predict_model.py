from src.config import MODEL_PATH 
import pickle 
import numpy as np 

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

weights = model["weights"]
mean = model["mean"]
std = model["std"]

student = np.array([[10, 85, 3]])

student = (student - mean)/std

student = np.hstack([np.ones((student.shape[0], 1)), student])

def sigmoid(z):
    return 1/(1+ np.exp(-z))

prob = sigmoid(student @ weights) 
y_pred = (prob >= 0.5).astype(int)

print("Predicted class: ", y_pred)
print("Pass probability: ", prob)
