import pickle 
import numpy as np 
from src.data.preprocess import load_data
from src.config import DATA_PATH, MODEL_PATH

def sigmoid(z):
    return 1/(1+np.exp(-z))

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

weights = model["weights"]
mean = model["mean"]
std = model["std"]

X, y = load_data(DATA_PATH)

X_norm = (X - mean)/std 

probs = sigmoid(X_norm @ weights)

preds = (probs >= 0.5).astype(int)

accuracy = np.mean(preds == y)
print("Accuracy: ", accuracy)
