import os
from flask import Flask, request, jsonify, render_template

# Initialize Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

# Attempt to import Mistral
try:
    from mistralai import Mistral
    # Initialize client inside the function to ensure it uses the latest environment variables
    def get_mistral_client():
        api_key = os.environ.get("MISTRAL_API_KEY")
        return Mistral(api_key=api_key)
except ImportError:
    Mistral = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    if Mistral is None:
        return jsonify({"solution": "Error: 'mistralai' library is missing from the server."}), 500
    
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"solution": "Please provide a query."}), 400

    try:
        client = get_mistral_client()
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        
        answer = response.choices[0].message.content
        return jsonify({"solution": answer})
        
    except Exception as e:
        return jsonify({"solution": f"AI Error: {str(e)}"}), 500
        
