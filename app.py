from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/")
def home():
    return "Hello, Flask!", 200

if __name__ == "__main__":
    # 0.0.0.0 lets it accept connections from anywhere (useful later for Docker)
    app.run(host="0.0.0.0", port=5000, debug=True)
