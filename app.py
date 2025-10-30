from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend API is running successfully!"

@app.route('/api/hello')
def hello():
    return {"message": "Hello from Flask API"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
