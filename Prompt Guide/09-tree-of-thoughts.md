# Tree of Thoughts (ToT)

Source: https://www.promptingguide.ai/techniques/tot

## Overview

For complex tasks requiring exploration or strategic lookahead, conventional prompting techniques prove insufficient. Yao et al. (2023) and Long (2023) introduced "Tree of Thoughts (ToT), a framework generalizing chain-of-thought prompting and encouraging exploration through intermediate reasoning steps for problem-solving with language models."

ToT maintains a tree structure where thoughts represent coherent language sequences serving as intermediate problem-solving steps. This methodology enables language models to self-evaluate progress toward solutions via deliberate reasoning. The model's capacity to generate and evaluate thoughts combines with search algorithms -- such as breadth-first search and depth-first search -- enabling systematic exploration with lookahead and backtracking capabilities.

## Task Configuration

Different tasks using ToT require defining candidate counts and thought/step quantities. For instance, the Game of 24 mathematical reasoning task decomposes into 3 steps involving intermediate equations. At each step, the best b=5 candidates remain selected.

## Breadth-First Search Implementation

For Game of 24 BFS in ToT, the model evaluates each thought candidate as "sure/maybe/impossible" regarding reaching 24. The approach "promotes correct partial solutions verdictable within few lookahead trials, eliminates impossible partial solutions based on common sense reasoning about magnitude, and retains uncertain candidates." Values are sampled 3 times per thought.

## Performance

ToT demonstrates substantial improvements over alternative prompting methods.

## Code Availability

Implementation code available at:
- https://github.com/princeton-nlp/tree-of-thought-llm
- https://github.com/jieyilong/tree-of-thought-puzzle-solver

## Comparative Analysis

Both Yao et al. (2023) and Long (2023) enhance LLM capabilities for complex problem-solving through tree search via multi-round conversations. Key differences include:

- **Yao et al. (2023)** employs DFS/BFS/beam search strategies -- generic, non-adaptive solution approaches
- **Long (2023)** proposes a "ToT Controller" trained via reinforcement learning, enabling problem-specific adaptation and continued evolution with fixed LLMs (similar to AlphaGo versus brute force approaches)

## Tree-of-Thought Prompting (Simplified)

Hulbert (2023) developed Tree-of-Thought Prompting, applying core ToT concepts as a simple prompting technique encouraging single-prompt intermediate thought evaluation. Example prompt:

```
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
The question is...
```

Sun (2023) benchmarked Tree-of-Thought Prompting through large-scale experiments and introduced PanelGPT -- a concept involving panel discussions among multiple LLMs.
