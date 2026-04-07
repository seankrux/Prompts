# Reflexion

Source: https://www.promptingguide.ai/techniques/reflexion

## Overview

Reflexion represents "a new paradigm for 'verbal' reinforcement that parameterizes a policy as an agent's memory encoding paired with a choice of LLM parameters" according to research by Shinn et al. (2023).

The framework converts environmental feedback into linguistic form -- termed **self-reflection** -- which becomes context for subsequent LLM agent episodes. This approach enables agents to learn rapidly from previous errors, yielding performance gains across advanced tasks.

## Framework Components

The Reflexion architecture comprises three distinct models:

1. **An Actor**: Generates text and actions based on state observations. Uses Chain-of-Thought and ReAct as foundational models, with added memory components providing contextual support.

2. **An Evaluator**: Scores Actor outputs by processing generated trajectories and producing reward scores. Different reward functions apply depending on task requirements (combining LLMs with rule-based heuristics).

3. **Self-Reflection**: An LLM-based component generating verbal reinforcement cues. It leverages reward signals, current trajectories, and persistent memory to deliver targeted feedback stored in long-term memory.

## Process Steps

The core Reflexion workflow involves:

a) Defining a task
b) Generating a trajectory
c) Evaluating outcomes
d) Performing reflection
e) Generating subsequent trajectories

The system extends ReAct by introducing self-evaluation, self-reflection, and memory mechanisms.

## Results

- **Sequential Decision-Making**: ReAct + Reflexion substantially outperforms baseline ReAct, completing 130/134 AlfWorld tasks using self-evaluation techniques.
- **Reasoning Tasks**: Reflexion + CoT surpasses both CoT alone and CoT with episodic memory on HotPotQA assessments across learning iterations.
- **Programming**: Reflexion generally exceeds previous state-of-the-art approaches on Python and Rust code writing tasks across MBPP, HumanEval, and Leetcode Hard benchmarks.

## When to Use Reflexion

Reflexion suits scenarios involving:

1. **Trial-and-error learning**: Agents improve through reflecting on mistakes and integrating knowledge into future decisions across decision-making, reasoning, and programming domains.

2. **Impractical traditional RL**: Offers lightweight alternatives without fine-tuning underlying models, reducing data and computational requirements.

3. **Nuanced feedback needs**: Verbal feedback provides specificity beyond scalar rewards typical in conventional RL.

4. **Interpretability priorities**: Explicit episodic memory enables clearer analysis of the learning process.

### Effective Task Applications

- Sequential decision-making in navigation and multi-step objectives
- Multi-document reasoning requirements
- Code generation benchmarks

### Limitations

- Depends on accurate self-evaluation capabilities
- Memory constraints using sliding windows; complex tasks may require advanced structures like vector embeddings or SQL databases
- Test-driven development challenges with non-deterministic functions and hardware-dependent outputs
