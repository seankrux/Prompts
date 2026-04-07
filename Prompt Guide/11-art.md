# Automatic Reasoning and Tool-use (ART)

Source: https://www.promptingguide.ai/techniques/art

## Overview

Automatic Reasoning and Tool-use (ART) represents a framework that integrates chain-of-thought prompting with external tool integration. This approach enables "a frozen LLM to automatically generate intermediate reasoning steps as a program."

## How ART Works

The methodology operates through several key steps:

1. **Demonstration Selection**: For new tasks, the system selects examples showcasing multi-step reasoning and tool integration from an existing task library

2. **Runtime Execution**: During testing, generation pauses whenever external tools require invocation, allowing their output to be incorporated before continuing

3. **Generalization**: The model generalizes from provided examples to decompose unfamiliar tasks and deploy tools appropriately in a zero-shot manner

## Key Advantages

The framework offers meaningful benefits:

- **Extensibility**: Humans can refine reasoning steps or introduce new tools by updating task and tool libraries
- **Performance**: Substantially outperforms few-shot prompting and automatic chain-of-thought across BigBench and MMLU benchmarks
- **Flexibility**: Exceeds hand-crafted prompts when incorporating human feedback
