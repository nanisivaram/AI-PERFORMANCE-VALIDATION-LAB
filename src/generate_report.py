import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
csv_file = project_root / "results" / "processed" / "latency_results.csv"
report_dir = project_root / "results" / "reports"
report_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv_file)

report_path = report_dir / "summary_report.md"

with report_path.open("w", encoding="utf-8") as f:
    f.write("# AI Performance Summary Report\n\n")
    f.write(f"- Total tests: {len(df)}\n")
    f.write(f"- Average latency: {round(df['wall_latency_s'].mean(), 3)} seconds\n")
    f.write(f"- Min latency: {round(df['wall_latency_s'].min(), 3)} seconds\n")
    f.write(f"- Max latency: {round(df['wall_latency_s'].max(), 3)} seconds\n")

print("Saved report to:", report_path)