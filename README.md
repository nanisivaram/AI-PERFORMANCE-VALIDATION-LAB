# AI Performance Lab
A local AI testing and performance evaluation lab built with Ollama and Python to measure latency, consistency, and system behavior of open-source language models under structured test conditions.

## Why this project
Modern AI assistants need more than correct answers. They must also respond quickly, behave consistently, and perform reliably under repeated usage. This project simulates a lightweight performance and validation workflow for latency-sensitive AI systems.

## Objectives
- Measure local model response latency
- Validate selected outputs using rule-based checks
- Test repeated-prompt consistency
- Observe basic system resource usage
- Save structured results and generate simple reports

## Tech Stack
- Ollama
- Python
- AI-testing
- performance-testing
- validation
- LLM
- QA
- requests
- pandas
- psutil
- pytest

## Project Structure
```text
AI PERFORMANCE & VALIDATION LAB/
│── README.md
│── requirements.txt
│── .gitignore
│── config/
│   ├── models.yaml
│   ├── test_profiles.yaml
│── prompts/
│   ├── short_prompts.json
│   ├── long_prompts.json
│   ├── consistency_prompts.json
│   ├── edge_case_prompts.json
│── src/
│   ├── run_single_test.py
│   ├── run_batch_tests.py
│   ├── measure_latency.py
│   ├── measure_resources.py
│   ├── validate_outputs.py
│   ├── simulate_network_conditions.py
│   ├── generate_report.py
│── results/
│   ├── raw/
│   ├── processed/
│   ├── charts/
│   ├── reports/
│── docs/
│   ├── test_plan.md
│   ├── methodology.md
│   ├── findings.md
│── scripts/
│   ├── setup_ollama.ps1
│   ├── run_all.ps1
│── tests/
│   ├── test_api_connection.py
│   ├── test_output_schema.py
```

## Test Coverage
### 1. Single prompt latency
Runs one prompt against a local Ollama model and measures wall-clock latency.
### 2. Batch prompt testing
Executes multiple prompts and stores structured results for later analysis.
### 3. Output validation
Checks selected responses against expected behavior using simple rule-based logic.
### 4. Consistency testing
Runs the same prompts multiple times to observe response stability and variation.
### 5. Resource observation
Collects basic CPU and memory usage snapshots during test runs.
### 6. Report generation
Creates a markdown summary of measured latency results.

## How to run
### 1. Start the model
```powershell
ollama run llama3.2
```
### 2. Run tests
```powershell
python src/run_single_test.py
python src/run_batch_tests.py
python src/measure_latency.py
python src/validate_outputs.py
python src/measure_resources.py
python src/generate_report.py
pytest tests
```
### 3. Optional full run
```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_all.ps1
```
## Current outputs
This project currently generates:
- raw batch results in JSON
- processed latency results in CSV
- a summary markdown report in `results/reports/`

## Engineering focus
This project is designed to demonstrate:
- local AI API testing
- performance measurement
- response validation
- repeatability
- engineering-style reporting

## Planned improvements
- cold-start vs warm-start comparison
- chart generation for latency trends
- richer output validation rules
- prompt-size performance comparison
- network-condition simulation
