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

    # Updated 2026 stable model list
    models_to_try = [
        'gemini-1.5-flash-latest', 
        'gemini-1.5-flash', 
        'gemini-pro'
    ]

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(user_query)
            return jsonify({"solution": response.text})
        except Exception as e:
            error_msg = str(e)
            # If it's a 404 (Model not found) or 429 (Quota), try the next one
            if "404" in error_msg or "429" in error_msg:
                continue 
            else:
                return jsonify({"solution": f"AI Notice: {error_msg}"})

    return jsonify({
        "solution": "All models are currently unavailable. Please check your API key or try again in a moment."
    })

app = app
