from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split


start = datetime.now()

# Load dataset
dataset = pd.read_csv("../dataset/dataset_school_van.csv")


X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values

print("X shape:", X)
print("y shape:", y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)