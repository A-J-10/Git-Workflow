from flask import Flask, jsonify, request, render_template
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

    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    return jsonify({
        "message": "Todo item submitted successfully",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
