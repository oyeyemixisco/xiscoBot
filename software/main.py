# Importing modules
import io, os, uuid
from flask import Flask, request, Response, render_template, redirect, session, url_for, flash, jsonify, send_file, abort
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

MAX_TPM = 8000
SAFE_MARGIN = 1000
MAX_OUTPUT_TOKENS = 512
MAX_HISTORY_MESSAGES = 6

def estimate_tokens(text):
    return len(text) // 4

def estimate_messages_tokens(messages):
    return sum(estimate_tokens(m["content"]) for m in messages)

def trim_history(messages):
    return messages[-MAX_HISTORY_MESSAGES:]


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message")
        history = data.get("history", []) 

        if not user_message:
            return {"error": "No message provided"}, 400

        system_prompt = {
            "role": "system",
            "content": (
                "You are Xisco, a helpful AI assistant. "
                "If asked who created you, say you were developed by Oyeyemi Dare Azeez, "
                "a Biometrics and Intelligent Vision graduate student at UPEC, France, "
                "and include this LinkedIn: https://www.linkedin.com/in/dare-azeez-oyeyemi-900652b0/. "
                "Always reply in the same language as the user. "
                "Keep responses concise."
            )
        }

        history = trim_history(history)

        messages = [system_prompt] + history + [
            {"role": "user", "content": user_message}
        ]

        input_tokens = estimate_messages_tokens(messages)
        max_allowed_output = MAX_TPM - SAFE_MARGIN - input_tokens
        max_tokens = max(128, min(MAX_OUTPUT_TOKENS, max_allowed_output))

        while max_tokens < 128 and len(history) > 0:
            history = history[1:]
            messages = [system_prompt] + history + [
                {"role": "user", "content": user_message}
            ]
            input_tokens = estimate_messages_tokens(messages)
            max_allowed_output = MAX_TPM - SAFE_MARGIN - input_tokens
            max_tokens = max(128, min(MAX_OUTPUT_TOKENS, max_allowed_output))

        
        def extract_content(chunk):
            if isinstance(chunk, tuple):
                chunk = chunk[0]
            try:
                return chunk.choices[0].delta.content
            except:
                return None


        def generate():
            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.7,
                max_tokens=max_tokens,
                top_p=1,
                reasoning_effort="low",
                stream=True,
            )

            for chunk in completion:
                content = extract_content(chunk)
                if content:
                    yield content

        return Response(generate(), content_type="text/plain")

    except Exception as e:
        print(f"Error: {e}")
        return {"response": "Sorry, I'm having trouble connecting right now."}, 500
    

# connect to the MySQL using the mysql.connector
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="chatbot"
    )
    return conn

# Route for the home page (to shows the form 'index.html')
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
