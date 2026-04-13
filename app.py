import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)

# --- SECURE API SETUP ---
# Render pulls this from the 'Environment Variables' you set
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- DATABASE SETUP ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///llumen_ai.db'
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

    # Log the search for your Admin dashboard
    new_log = SearchLog(query=user_query)
    db.session.add(new_log)
    db.session.commit()

    try:
        response = model.generate_content(user_query)
        return jsonify({"solution": response.text})
    except Exception as e:
        return jsonify({"solution": "Error: Check your API Key in Render."})

@app.route('/admin')
def admin():
    logs = SearchLog.query.order_by(SearchLog.timestamp.desc()).all()
    return render_template('admin.html', logs=logs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
