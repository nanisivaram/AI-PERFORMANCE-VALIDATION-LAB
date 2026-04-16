import requests

def test_generate_response_schema():
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": "Say hello",
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    data = response.json()

    assert "response" in data
    assert "total_duration" in data
    assert isinstance(data["response"], str)