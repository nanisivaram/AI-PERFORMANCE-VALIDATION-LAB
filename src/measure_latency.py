import json
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "results" / "raw" / "batch_results.json"
output_dir = project_root / "results" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

with input_file.open("r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
csv_path = output_dir / "latency_results.csv"
df.to_csv(csv_path, index=False)

print("Average latency:", round(df["wall_latency_s"].mean(), 3), "seconds")
print("Min latency:", round(df["wall_latency_s"].min(), 3), "seconds")
print("Max latency:", round(df["wall_latency_s"].max(), 3), "seconds")
print("Saved CSV to:", csv_path)