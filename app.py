from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Safe import attempt
try:
    from mistralai import Mistral
    MISTRAL_AVAILABLE = True
except ImportError:
    MISTRAL_AVAILABLE = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if not MISTRAL_AVAILABLE:
        return jsonify({"solution": "Error: Mistral library not found on server."}), 500
    
    data = request.get_json()
    user_query = data.get('query', '')
    
    try:
        api_key = os.environ.get("MISTRAL_API_KEY")
        client = Mistral(api_key=api_key)
        
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        return jsonify({"solution": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"solution": f"AI Error: {str(e)}"}), 500
        
