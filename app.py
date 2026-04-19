import os
from flask import Flask, render_template, request, jsonify
from mistralai import Mistral

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        # If this part crashes, we catch it
        data = request.get_json()
        query = data.get('query', '')
        
        # Test Mistral
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            return jsonify({"solution": "Error: API Key missing in Vercel settings!"})
            
        client = Mistral(api_key=api_key)
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": query}]
        )
        return jsonify({"solution": response.choices[0].message.content})
        
    except Exception as e:
        # THIS WILL SHOW THE ERROR ON YOUR PHONE SCREEN
        return jsonify({"solution": f"CRITICAL ERROR: {str(e)}"})

if __name__ == '__main__':
    app.run()
    
