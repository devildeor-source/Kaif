import os
from flask import Flask, request, jsonify, render_template
from mistralai import Mistral

app = Flask(__name__, template_folder='templates', static_folder='static')

# Use the environment variable name exactly as it will be in Vercel
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
        # Mistral small is fast and efficient for mobile study tools
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": user_query}]
        )
        
        answer = response.choices[0].message.content
        pacing = "\n\n---\n*Tap again in 5-6s to keep connection stable.*"
        
        return jsonify({"solution": answer + pacing})
    except Exception:
        # Return 503 so your index.html's 'cache: no-store' 
        # logic can handle the reset smoothly
        return '', 503

if __name__ == '__main__':
    app.run(debug=True)
    
