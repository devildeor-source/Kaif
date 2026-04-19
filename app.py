import os
from flask import Flask, request, jsonify, render_template
from mistralai import Mistral

# Initialize Flask
app = Flask(__name__)

# Initialize Mistral client
# It is better to initialize the client once globally if possible
def get_client():
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY is not set in environment variables.")
    return Mistral(api_key=api_key)

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
        client = get_client()
        # We explicitly set a timeout here. Vercel functions have limits;
        # if Mistral takes longer than 10-15 seconds, we want it to error 
        # out rather than hang the browser session indefinitely.
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}],
            timeout=15.0 
        )
        
        answer = response.choices[0].message.content
        return jsonify({"solution": answer})
        
    except Exception as e:
        # Returning the error helps you see exactly why it failed in the browser
        return jsonify({"solution": f"Server Error: {str(e)}"}), 500
        
