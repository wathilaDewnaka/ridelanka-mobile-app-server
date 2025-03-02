import joblib
import pandas as pd

model = joblib.load("trained_model.pkl")
print("Model loaded successfully!")

def predict_price(from_city, to_city, vehicle_type, service_type, distance):
    new_data = pd.DataFrame([[from_city, to_city, vehicle_type, service_type, distance]],
                            columns=['From City', 'To City', 'Vehicle Type', 'Service Type', 'Total Distance (km)'])
    return model.predict(new_data)[0]