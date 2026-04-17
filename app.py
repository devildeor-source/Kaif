import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- API SETUP ---
# Strip removes any hidden spaces from your Vercel settings
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

if API_KEY:
    genai.configure(api_key=API_KEY)
    # Using 'gemini-1.5-flash' is the most stable for Vercel
    model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "System Error: API Key not found in Vercel."})
    
    data = request.json
    user_query = data.get('query')

    try:
        response = model.generate_content(user_query)
        return jsonify({"solution": response.text})
    except Exception as e:
        return jsonify({"solution": f"AI Error: {str(e)}"})

# Crucial for Vercel to recognize the app object
app = app
