from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/")
def home():
    return "Hello, Flask!", 200


# ✅ New: POST /data
@app.post("/data")
def receive_data():
    # Get JSON payload
    data = request.get_json()

    # Basic validation
    if not data or "name" not in data:
        return jsonify(error="Missing 'name' field"), 400

    name = data["name"]
    return jsonify(message=f"Data received for {name}"), 200


if __name__ == "__main__":
    # 0.0.0.0 lets it accept connections from anywhere (useful later for Docker)
    app.run(host="0.0.0.0", port=5000, debug=True)
