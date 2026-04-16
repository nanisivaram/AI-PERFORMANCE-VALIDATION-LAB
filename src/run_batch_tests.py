import json
import time
from pathlib import Path
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

project_root = Path(__file__).resolve().parent.parent
prompts_file = project_root / "prompts" / "short_prompts.json"

with prompts_file.open("r", encoding="utf-8") as f:
    prompts = json.load(f)

results = []

for idx, prompt in enumerate(prompts, start=1):
    start = time.time()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    end = time.time()
    response.raise_for_status()
    data = response.json()

    result = {
        "test_id": f"T{idx:03d}",
        "prompt": prompt,
        "response": data.get("response", "").strip(),
        "wall_latency_s": round(end - start, 3),
        "total_duration_ns": data.get("total_duration"),
        "load_duration_ns": data.get("load_duration"),
        "prompt_eval_duration_ns": data.get("prompt_eval_duration"),
        "eval_duration_ns": data.get("eval_duration")
    }

    results.append(result)
    print(f"{result['test_id']} done in {result['wall_latency_s']} s")

raw_dir = project_root / "results" / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

output_file = raw_dir / "batch_results.json"
with output_file.open("w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved results to: {output_file}")