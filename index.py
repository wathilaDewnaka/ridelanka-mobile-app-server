from flask import Flask, request, jsonify
import ml.chat
import ml.getPrice as price
import ml.predictor as pre

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = ml.chat.get_chatbot_response(user_message)
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
    app.run(host="0.0.0.0", port=5000)