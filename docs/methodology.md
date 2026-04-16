# Methodology
This project evaluates a local Ollama-hosted language model using Python-based test scripts.

## Approach
The testing workflow is designed to measure:
- wall-clock latency
- API timing metadata
- response consistency
- basic output correctness
- basic system resource usage

## Execution Flow
1. Send prompts to the local Ollama API
2. Capture response text and timing information
3. Save raw results
4. Process latency results into structured files
5. Validate selected outputs with simple rules
6. Generate summary reports

## Scope
This project focuses on local model testing and does not currently simulate:
- real mobile hardware
- device battery impact
- GPU profiling
- production network throttling