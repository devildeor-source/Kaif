import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This route lets us verify if the server is even running at all
@app.route('/health')
def health():
    return "The server is alive!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        # Step 1: Check if Environment Variable exists
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            return jsonify({"solution": "CRITICAL ERROR: MISTRAL_API_KEY is not set in Vercel settings."})

        # Step 2: Attempt import (to see if the library is actually found)
        from mistralai import Mistral
        
        # Step 3: Perform dummy call
        client = Mistral(api_key=api_key)
        # This will tell us if the library usage itself is the problem
        return jsonify({"solution": "Connection successful, but search logic paused for testing."})
        
    except Exception as e:
        # THIS WILL PRINT THE EXACT ERROR ON YOUR PHONE SCREEN
        return jsonify({"solution": f"DETAILED ERROR: {str(e)}"})

if __name__ == '__main__':
    app.run()
    
