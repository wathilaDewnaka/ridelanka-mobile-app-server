from datetime import datetime

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

start = datetime.now()

# Load dataset
dataset = pd.read_csv("../dataset/dataset_school_van.csv")


X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values

print("X shape:", X)
print("y shape:", y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), X.columns[:4])  # Encode first 4 columns
    ],
    remainder='passthrough'  # Keep numerical column (Total Distance)
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

joblib.dump(model, "trained_model.pkl")
print("Model saved successfully!")

def predict_price(from_city, to_city, vehicle_type, service_type, distance):
    new_data = pd.DataFrame([[from_city, to_city, vehicle_type, service_type, distance]],
                            columns=X.columns)
    return model.predict(new_data)[0]

# Example: Predict price for new input
predicted_price = predict_price('Colombo', 'Gampaha', 'Van', 'School', 30)
print(f"Predicted Monthly Subscription: Rs {predicted_price:.2f}")


end = datetime.now()
elapsed_time = end - start

minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
print(f"Time elapsed: {int(minutes)} minutes and {seconds:.2f} seconds")