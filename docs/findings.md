# Findings

## Initial observations

- Local model responses can be measured reliably through the Ollama API
- Wall-clock latency varies by prompt size and response length
- Repeated prompts can be used to study response consistency
- Basic validation checks help verify correctness for deterministic prompts

## Next analysis steps

- compare cold-start and warm-start latency
- generate charts for latency trends
- expand validation rules for format-sensitive prompts
- measure behavior across short and long prompt sets