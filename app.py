import os
from flask import Flask, render_template, request, jsonify
from mistralai.client import MistralClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        query = data.get('query', '')
        api_key = os.environ.get("MISTRAL_API_KEY")
        
        client = MistralClient(api_key=api_key)
        response = client.chat(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": query}]
        )
        return jsonify({"solution": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"solution": f"Error: {str(e)}"})

if __name__ == '__main__':
    # Hugging Face Spaces must bind to 0.0.0.0 and port 7860
    app.run(host='0.0.0.0', port=7860)
    
