# Test Plan

## Objective
Measure local AI model behavior for latency, consistency, and validation under structured test conditions.

## Test Areas
### 1. Single Prompt Test
- Verify local API works
- Measure one response latency

### 2. Batch Prompt Test
- Run multiple prompts
- Save results to JSON and CSV

### 3. Output Validation
- Check deterministic prompts for expected output
- Example: `25 * 17 = 425`

### 4. Consistency Test
- Run the same prompt multiple times
- Observe variation across outputs

### 5. Resource Observation
- Capture CPU and memory snapshot during runs

### 6. Cold vs Warm Latency
- Compare first run latency against repeated runs

## Environment
- Windows
- Ollama local runtime
- Python test harness
- Model: llama3.2