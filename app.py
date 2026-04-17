import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- API SETUP ---
# We use .strip() to ensure no accidental spaces break the key
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "API Key is missing in Vercel settings."})
    
    data = request.json
    user_query = data.get('query')

    try:
        response = model.generate_content(user_query)
        return jsonify({"solution": response.text})
    except Exception as e:
        return jsonify({"solution": f"AI Error: {str(e)}"})

# Vital for Vercel's Python runtime
app = app
