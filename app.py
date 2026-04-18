import os
from flask import Flask, request, jsonify, render_template
from mistralai import Mistral

app = Flask(__name__, template_folder='templates', static_folder='static')

# Ensure MISTRAL_API_KEY is in Vercel Environment Variables
api_key = os.environ.get("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    user_query = data.get('query', '')
    
    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        return jsonify({"solution": response.choices[0].message.content})
    except Exception:
        return '', 503

if __name__ == '__main__':
    app.run(debug=True)
    
