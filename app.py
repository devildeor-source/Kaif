import os
import sys
# Force python to check the virtual environment paths
sys.path.append('/vercel/path0/.vercel/python/.venv/lib/python3.12/site-packages')

from flask import Flask, request, jsonify, render_template
from mistralai import Mistral


app = Flask(__name__, template_folder='templates', static_folder='static')

# Ensure the API Key is retrieved from Vercel's Environment Variables
api_key = os.environ.get("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"solution": "Please provide a query."}), 400

    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        # Success
        return jsonify({"solution": response.choices[0].message.content})
    except Exception as e:
        # Returns 500 so you can see the error in Vercel logs if it fails
        return jsonify({"solution": f"Server Error: {str(e)}"}), 500

# DO NOT include app.run() or app=app
# Vercel handles the application startup automatically.
