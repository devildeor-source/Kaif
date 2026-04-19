import os
from flask import Flask, request, jsonify, render_template
from mistralai import Mistral

app = Flask(__name__)

# Initialize the Mistral client using the API key from environment variables
def get_client():
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY is not set.")
    return Mistral(api_key=api_key)

@app.route('/')
def index():
    # This renders your index.html file
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        user_query = data.get('query', '')
        
        if not user_query:
            return jsonify({"solution": "Query cannot be empty."}), 400

        client = get_client()
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}],
            timeout=20.0
        )
        
        answer = response.choices[0].message.content
        return jsonify({"solution": answer})

    except Exception as e:
        # This will return the actual error so you can see why it crashes
        return jsonify({"solution": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
    
