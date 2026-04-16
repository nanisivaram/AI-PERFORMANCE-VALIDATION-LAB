import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "results" / "raw" / "batch_results.json"

with input_file.open("r", encoding="utf-8") as f:
    results = json.load(f)

for item in results:
    prompt = item["prompt"]
    response = item["response"]

    passed = True
    notes = ""

    if "25 * 17" in prompt and "425" not in response:
        passed = False
        notes = "Expected 425"

    print({
        "test_id": item["test_id"],
        "pass": passed,
        "notes": notes
    })