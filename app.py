from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask backend!"})

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    return jsonify({"received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
