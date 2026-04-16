import time
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"
PROMPT = "Explain AI in one sentence."

simulated_delays = [0, 1, 2]

for delay in simulated_delays:
    print(f"\nRunning with simulated pre-request delay: {delay} second(s)")
    time.sleep(delay)

    start = time.time()
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": PROMPT,
            "stream": False
        },
        timeout=120
    )
    end = time.time()

    response.raise_for_status()
    data = response.json()

    print("Response:", data.get("response", "").strip())
    print("Observed latency:", round(end - start, 3), "seconds")