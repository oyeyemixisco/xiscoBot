# Importing modules
import io, os, uuid
from flask import Flask, request, render_template, redirect, session, url_for, flash, jsonify, send_file, abort
import mysql.connector
import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# declaring Flask app
app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Create the completion request to Groq
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b", # Fast and capable model
            messages=[
                {"role": "system", "content": 
                "You are Xisco, a helpful AI assistant. "
                "If asked who created you, say you were developed by Oyeyemi Dare Azeez, a Biometrics and Intelligent Vision graduate student at UPEC, France, and include this LinkedIn: https://www.linkedin.com/in/dare-azeez-oyeyemi-900652b0/. "
                "Always reply in the same language as the user. "
                "Optionally suggest next steps briefly."
                },
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            reasoning_effort="low",
        )

        response_text = completion.choices[0].message.content
        return jsonify({"response": response_text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, I'm having trouble connecting to my brain right now."}), 500
    
# connect to the MySQL using the mysql.connector
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="chatbot"
    )
    return conn

# Route for the home page 
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')
    
# Route for the chat dashboard
@app.route('/home')
def home():
    return render_template('index.html')

# route for logout
@app.route('/lock')
def lock():
    return render_template('lock-screen.html')

# Route for the register page  
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
