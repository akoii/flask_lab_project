from app import app  # import the Flask app from your main file

# Test the home route
def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

# Test the health route
def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "ok"

# Test the POST /data route
def test_data_post():
    client = app.test_client()

    # Send correct JSON
    valid_response = client.post("/data", json={"name": "Alice"})
    assert valid_response.status_code == 200
    assert b"Data received" in valid_response.data

    # Send invalid JSON (missing 'name')
    invalid_response = client.post("/data", json={})
    assert invalid_response.status_code == 400
    assert b"Missing" in invalid_response.data
