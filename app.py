import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder='templates')

# Configure your key from Vercel environment variables
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if API_KEY:
    genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "API Key is missing. Add it to Vercel Settings."})
    
    user_query = request.json.get('query', '')

    # 2026 Stable Model List: If one fails, it tries the next one automatically
    models_to_try = [
        'gemini-3.1-flash',       # Newest 2026 Free Tier
        'gemini-3.0-flash',       # Very stable 
        'gemini-2.5-flash',       # Backup
        'gemini-1.5-flash-latest' # Emergency fallback
    ]

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(user_query)
            return jsonify({"solution": response.text})
        except Exception as e:
            error_str = str(e)
            # If the error is Quota (429) or Model Not Found (404), move to next model
            if "429" in error_str or "404" in error_str:
                continue 
            return jsonify({"solution": f"AI Notice: {error_str}"})

    return jsonify({"solution": "All models are currently at their free limit. Please try again in 60 seconds."})

app = app
