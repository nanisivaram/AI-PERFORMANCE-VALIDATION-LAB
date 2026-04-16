import requests

def test_ollama_api_connection():
    response = requests.get("http://localhost:11434")
    assert response.status_code in [200, 404]