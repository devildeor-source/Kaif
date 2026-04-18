import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

# Ensure your API Key is set correctly in Vercel Environment Variables
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if API_KEY:
    genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not API_KEY:
        return jsonify({"solution": "API Configuration Error."})
        
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"solution": "Please provide a query."})

    # The "Anti-Limit" Queue: 
    # This list covers every available model that can run your requests.
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
            
            # If the response is valid, return it immediately
            return jsonify({"solution": response.text})
            
        except Exception:
            # If ANY model fails (limit reached), we silently jump to the next one
            continue
            
    # If the code reaches here, ALL models are busy.
    # Instead of an error message, we return a friendly "retry" prompt.
    return jsonify({"solution": "LLUMEN AI is upgrading its connection... please tap search again in 5 seconds."})

if __name__ == '__main__':
    app.run(debug=True)
    
