import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder='templates')

# --- CONFIGURATION ---
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

if API_KEY:
    genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "Error: API Key is missing in Vercel settings."})
    
    data = request.json
    user_query = data.get('query', '')

    if not user_query:
        return jsonify({"solution": "Please enter a message."})

    # List of models to try in order of quality/availability in 2026
    # If the first one has no quota, it automatically jumps to the next
    models_to_try = [
        'gemini-2.0-flash', 
        'gemini-1.5-flash', 
        'gemini-1.5-pro',
        'gemini-1.0-pro'
    ]

    last_error = ""
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(user_query)
            # If successful, return immediately
            return jsonify({"solution": response.text})
        except Exception as e:
            error_msg = str(e)
            last_error = error_msg
            # If it's a Quota (429) error, try the next model
            if "429" in error_msg or "quota" in error_msg.lower():
                continue 
            else:
                # If it's a different error (like safety filters), stop and show it
                return jsonify({"solution": f"AI Notice: {error_msg}"})

    # If we get here, it means all models in the list failed
    return jsonify({
        "solution": f"All free-tier models are currently busy or out of quota. Please wait a few minutes. (Last error: {last_error})"
    })

# Required for Vercel
app = app
    
