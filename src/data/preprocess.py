import pandas as pd
import numpy as np 

def load_data(path):
    df = pd.read_csv(path)

    X = df[['Hours Studied', 'Attendance%', 'Previous GPA']].values 
    y = df[['Passed(0/1)']].values.reshape(-1, 1)
    return X, y

def normalize_features(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    X_norm = (X - mean)/std
    X_norm = np.hstack([np.ones((X_norm.shape[0], 1)), X_norm])

    return X_norm, mean, std
