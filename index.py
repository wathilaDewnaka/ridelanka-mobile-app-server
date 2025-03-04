from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = "" #Get the bot response
    return jsonify({"response": bot_response})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    pass


if _name_ == '_main_':
    app.run(debug=False)