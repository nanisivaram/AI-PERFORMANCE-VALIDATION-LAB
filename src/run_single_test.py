import requests
import time

start = time.time()

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "Explain AI in one sentence.",
        "stream": False
    }
)

end = time.time()

data = response.json()

print("Response:", data["response"])
print("Latency:", round(end - start, 3), "seconds")