import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if API_KEY:
    genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    user_query = data.get('query', '')
    models = ['gemini-3.1-flash', 'gemini-3.0-flash', 'gemini-1.5-flash']
    
    for model_name in models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(user_query)
            # Answer + Pacing Reminder
            return jsonify({"solution": response.text + "\n\n---\n*Tap again in 5-6s to keep connection stable.*"})
        except Exception:
            continue
            
    return '', 503

if __name__ == '__main__':
    app.run(debug=True)
    
