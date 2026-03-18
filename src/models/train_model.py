import numpy as np 
import pickle 
from src.data.preprocess import load_data, normalize_features 
from src.config import DATA_PATH, MODEL_DIR, MODEL_PATH

def sigmoid(z):
    return 1/(1+ np.exp(-z))

#we are training a Logistic Regression model 
def train(X, y, epochs=5000, lr=0.01):
    weights = np.zeros((X.shape[1], 1))
    for epoch in range(epochs):
        z = X @ weights 

        y_pred = sigmoid(z)

        gradient = (X.T @ (y_pred - y))/len(y)
        
        weights = weights - (lr * gradient)

    return weights 

X, y = load_data(DATA_PATH)

X_norm, mean, std = normalize_features(X) 

weights = train(X_norm, y)

model = {
    "weights": weights,
    "mean": mean,
    "std": std
}

MODEL_DIR.mkdir(parents=True, exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)
