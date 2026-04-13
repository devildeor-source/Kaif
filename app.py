import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)

# --- SECURE API SETUP ---
# We use .strip() to automatically remove any accidental spaces you might have pasted in Render
raw_key = os.environ.get("GEMINI_API_KEY", "")
API_KEY = raw_key.strip()

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        print(f"Setup Error: {e}")
else:
    print("Environment Variable 'GEMINI_API_KEY' not found.")

# --- DATABASE SETUP ---
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'llumen_ai.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SearchLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    user_query = data.get('query')

    if not user_query:
        return jsonify({"solution": "The search was empty."})

    # Log the search
    try:
        new_log = SearchLog(query=user_query)
        db.session.add(new_log)
        db.session.commit()
    except:
        pass

    if not API_KEY:
        return jsonify({"solution": "Error: GEMINI_API_KEY is not set in Render Environment Variables."})

    try:
        # The AI processing
        response = model.generate_content(user_query)
        return jsonify({"solution": response.text})
    except Exception as e:
        # This will tell us the EXACT error from Google (e.g., 'Expired Key' or 'Invalid Key')
        return jsonify({"solution": f"AI Error: {str(e)}"})

@app.route('/admin')
def admin():
    logs = SearchLog.query.order_by(SearchLog.timestamp.desc()).all()
    return render_template('admin.html', logs=logs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
