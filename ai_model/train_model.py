print("Model Saved Successfully")

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv("health_data.csv")

X = df[["glucose", "haemoglobin", "cholesterol"]]
y = df["risk"]

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model Trained Successfully")