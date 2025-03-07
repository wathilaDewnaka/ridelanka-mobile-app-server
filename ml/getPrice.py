import joblib
import pandas as pd

def getPricePrediction(start, end, type, service, km):
    model = joblib.load("trained_model.pkl")

    def predict_price(from_city, to_city, vehicle_type, service_type, distance):
        new_data = pd.DataFrame([[from_city, to_city, vehicle_type, service_type, distance]],
                                columns=['From City', 'To City', 'Vehicle Type', 'Service Type', 'Total Distance (km)'])
        return model.predict(new_data)[0]

    predicted_price = predict_price('makola', 'kiribathgoda', 'Van', 'School', 25)
    print(f"Predicted Monthly Subscription: Rs {predicted_price:.2f}")
    return f"{round(predicted_price)}"
