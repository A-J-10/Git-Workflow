from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

@app.route('/api')
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/')
def home():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    return {
        "message": "Todo item received",
        "data": data
    }

if __name__ == '__main__':
    app.run(debug=True)
