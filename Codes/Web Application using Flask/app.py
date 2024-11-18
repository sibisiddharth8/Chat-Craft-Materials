from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# Set your API key here
API_KEY = "your API key"

# Configure the Gemini API with the API key
genai.configure(api_key=API_KEY)

# Create the model with generation configurations
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chat_session.send_message(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)