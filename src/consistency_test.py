import json
import time
from pathlib import Path
import requests
from collections import Counter

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

project_root = Path(__file__).resolve().parent.parent
prompts_file = project_root / "prompts" / "consistency_prompts.json"

with prompts_file.open("r", encoding="utf-8") as f:
    prompts = json.load(f)

for prompt in prompts:
    outputs = []
    print(f"\nPrompt: {prompt}")

    for i in range(5):
        start = time.time()
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        end = time.time()

        response.raise_for_status()
        data = response.json()

        output = data.get("response", "").strip()
        outputs.append(output)

        print(f"Run {i+1}: {round(end-start,3)}s | {output}")

    counts = Counter(outputs)
    print("Unique outputs:", len(counts))
    print("Most common output:", counts.most_common(1)[0][0])