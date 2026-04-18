import os
from flask import Flask, request, jsonify, render_template
from mistralai import Mistral

# Initialize Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

# Initialize Mistral Client
# Ensure MISTRAL_API_KEY is set in Vercel Project Settings > Environment Variables
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
        # Use mistral-small-latest for fast, efficient response
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        
        answer = response.choices[0].message.content
        return jsonify({"solution": answer})
        
    except Exception as e:
        # Return 500 so you can inspect the error in Vercel Runtime Logs
        return jsonify({"solution": f"AI Service Error: {str(e)}"}), 500

# NOTE: Do not include app.run() or app = app. 
# Vercel handles server initialization automatically via the 'app' instance.
