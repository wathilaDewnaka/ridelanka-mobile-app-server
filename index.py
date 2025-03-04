from flask import Flask, request, jsonify
import os

import ml.chat as chat
import ml.getPrice as price
import ml.predictor as pre

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = chat.get_chatbot_response(user_message)
    return jsonify({"response": bot_response})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    start = data.get("start", "")
    end = data.get("end", "")
    type = data.get("type", "")
    service = data.get("service", "")
    km = int(data.get("distance", ""))
    return jsonify({"price": price.getPricePrediction(start, end, type, service, km)})


if __name__ == '__main__':
    # Define the path for the model file
    model_file = "trained_model.pkl"

    # Check if the model already exists
    if not os.path.exists(model_file):
        pre.trainData()

    app.run()