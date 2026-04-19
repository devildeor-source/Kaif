import os
from flask import Flask, render_template, request, jsonify
# This import matches mistralai version 1.0.0
from mistralai import Mistral

app = Flask(__name__)

@app.route('/health')
def health():
    return "The server is alive!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        user_query = data.get('query', '')
        
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            return jsonify({"solution": "Error: API Key missing."})

        # Initialize the client
        client = Mistral(api_key=api_key)
        
        # Make the request
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        
        return jsonify({"solution": response.choices[0].message.content})
        
    except Exception as e:
        return jsonify({"solution": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run()
    
