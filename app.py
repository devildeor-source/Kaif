from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    # This is a test to see if the server communicates with your phone
    return jsonify({"solution": "Server is working perfectly."})
    
