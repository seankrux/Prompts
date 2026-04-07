# Automatic Prompt Engineer (APE)

Source: https://www.promptingguide.ai/techniques/ape

## Overview

Automatic Prompt Engineer represents a framework for creating and selecting instructions automatically. "The instruction generation problem is framed as natural language synthesis addressed as a black-box optimization problem using LLMs."

## How APE Works

The process involves several key steps:

1. A large language model generates instruction candidates from output demonstrations
2. These candidate solutions direct the search procedure
3. A target model executes the instructions
4. The most suitable instruction is selected based on evaluation scores

## Key Discovery

APE found a superior zero-shot Chain-of-Thought prompt compared to human-created alternatives. The discovered prompt states:

> "Let's work this out in a step by step way to be sure we have the right answer."

This formulation improved performance on MultiArith and GSM8K benchmarks.

## Related Research Areas

- **Prompt-OIRL** - Uses offline inverse reinforcement learning for query-dependent prompts
- **OPRO** - Employs LLMs to optimize prompts
- **AutoPrompt** - Creates prompts automatically through gradient-guided search
- **Prefix Tuning** - Lightweight fine-tuning alternative with trainable prefixes
- **Prompt Tuning** - Learns soft prompts via backpropagation
