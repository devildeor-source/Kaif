from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        # Step 1: Check if library exists
        import mistralai
        
        # Step 2: Check if key exists
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            return jsonify({"solution": "Error: MISTRAL_API_KEY is not set in Vercel settings!"})
            
        # Step 3: Try to initialize
        from mistralai import Mistral
        client = Mistral(api_key=api_key)
        
        return jsonify({"solution": "Library and Key found! Ready to connect."})
        
    except ImportError:
        return jsonify({"solution": "CRITICAL: 'mistralai' library is NOT installed on the server."})
    except Exception as e:
        return jsonify({"solution": f"General Error: {str(e)}"})
        
