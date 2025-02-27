import google.generativeai as genai

def initialize_chatbot():
    genai.configure(api_key="AIzaSyCNm3Z12_CFRYUxupMKeoqnXXAoJnFPhEk")
    
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
        system_instruction=(
            "1. Introduction\n\n"
            "The RideLanka Chatbot is designed to assist users in navigating the RideLanka mobile application by "
            "providing clear and user-friendly guidance on various app operations. The chatbot will be trained using "
            "the Gemini API to ensure accurate and helpful responses.\n\n"
            "2. Chatbot Requirements\n\n"
            "User-friendly: Responses should be easy to understand.\n"
            "Process-oriented: Guide users step by step on how to complete actions.\n"
            "Concise: Avoid lengthy explanations, focusing on essential steps.\n"
            "Friendly Tone: Maintain a warm and helpful tone.\n\n"
            "3. Sample Training Data\n\n"
            "User Registration\n\n"
            "Intent: How to register as a user?\n"
            "Response: \"Hello! 👋 To register as a user:\n"
            "1. Open the RideLanka app.\n"
            "2. Tap 'Sign Up' on the home screen.\n"
            "3. Enter your name, email, and phone number.\n"
            "4. Set a secure password and confirm it.\n"
            "5. Tap 'Register'. Done! 🎉 Now, log in and start using the app. 🚀\"\n\n"
            "Booking a Ride\n\n"
            "Intent: How do I book a ride?\n"
            "Response: \"Hey there! 🚖 Booking a ride is easy:\n"
            "1. Open the app and log in.\n"
            "2. Enter your pickup and drop-off location.\n"
            "3. Choose a vehicle type.\n"
            "4. Tap 'Confirm Booking'.\n"
            "5. You'll see the driver details and can track your ride. Safe travels! 🚀\""
        ),
    )
    
    return model

def start_chatbot():
    model = initialize_chatbot()
    history = []
    print("Bot: Hello, how can I help you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day!")
            break
        
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(user_input)
        model_response = response.text
        
        print(f'Bot: {model_response}\n')
        
        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "model", "parts": [model_response]})

if __name__ == "__main__":
    start_chatbot()
