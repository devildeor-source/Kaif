import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

# API Key Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if API_KEY:
    genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "API Configuration Error."}), 500
        
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"solution": "Please provide a query."}), 400

    # The Failover Pool: These models will be tried in sequence until one works
    models_to_try = [
        'gemini-3.1-flash', 
        'gemini-3.0-flash', 
        'gemini-2.5-flash', 
        'gemini-1.5-flash',
        'gemini-1.5-pro'
    ]
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(user_query)
            return jsonify({"solution": response.text})
        except Exception:
            # If a model is busy, we silently fail and try the next one immediately
            continue
            
    # If all models in the pool are busy, return 503 so the frontend can reset
    return jsonify({"solution": "Busy"}), 503

if __name__ == '__main__':
    app.run(debug=True)
    
