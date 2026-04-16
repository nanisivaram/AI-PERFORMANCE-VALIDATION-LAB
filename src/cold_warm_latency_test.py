import time
import requests
from pathlib import Path
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"
PROMPT = "Explain AI in one sentence."

project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "results" / "reports"
output_dir.mkdir(parents=True, exist_ok=True)

results = []

# Cold-start run
start = time.time()
response = requests.post(
    OLLAMA_URL,
    json={"model": MODEL, "prompt": PROMPT, "stream": False},
    timeout=120
)
end = time.time()
response.raise_for_status()
data = response.json()

results.append({
    "run_type": "cold_start",
    "wall_latency_s": round(end - start, 3),
    "total_duration_ns": data.get("total_duration"),
    "load_duration_ns": data.get("load_duration"),
    "prompt_eval_duration_ns": data.get("prompt_eval_duration"),
    "eval_duration_ns": data.get("eval_duration")
})

# Warm runs
for i in range(3):
    start = time.time()
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": PROMPT, "stream": False},
        timeout=120
    )
    end = time.time()
    response.raise_for_status()
    data = response.json()

    results.append({
        "run_type": f"warm_run_{i+1}",
        "wall_latency_s": round(end - start, 3),
        "total_duration_ns": data.get("total_duration"),
        "load_duration_ns": data.get("load_duration"),
        "prompt_eval_duration_ns": data.get("prompt_eval_duration"),
        "eval_duration_ns": data.get("eval_duration")
    })

report_file = output_dir / "cold_warm_latency_results.json"
with report_file.open("w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Cold vs Warm Latency Results:")
for item in results:
    print(item)

print(f"\nSaved to: {report_file}")