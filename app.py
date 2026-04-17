import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- API SETUP ---
# Grabs the key from Vercel and removes any accidental spaces
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

if API_KEY:
    genai.configure(api_key=API_KEY)
    # Using 'gemini-2.0-flash' which is the standard for 2026 apps
    # Gemini 2.5 Flash is the most stable free model right now
model = genai.GenerativeModel('gemini-2.5-flash')

    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "Configuration Error: API Key not found in Vercel settings."})
    
    data = request.json
    user_query = data.get('query', '')

    if not user_query:
        return jsonify({"solution": "Please enter a prompt."})

    try:
        response = model.generate_content(user_query)
        return jsonify({"solution": response.text})
    except Exception as e:
        return jsonify({"solution": f"AI Error: {str(e)}"})

# Vital for Vercel's Python runtime to locate the application
app = app
