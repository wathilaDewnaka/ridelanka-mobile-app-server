from datetime import datetime
import pandas as pd


start = datetime.now()

# Load dataset
dataset = pd.read_csv("../dataset/dataset_school_van.csv")


X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values

print("X shape:", X)
print("y shape:", y)