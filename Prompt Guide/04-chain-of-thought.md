# Chain-of-Thought Prompting

Source: https://www.promptingguide.ai/techniques/cot

## Chain-of-Thought (CoT) Prompting

The technique, introduced in Wei et al. (2022), leverages "intermediate reasoning steps" to solve complex problems. When combined with few-shot prompting, it improves performance on demanding tasks requiring analytical thinking.

### Example Problem

Determine if odd numbers in a group sum to an even number.

**Prompt:**
```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
A:
```

**Output:**
```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

This is an emergent ability that arises with sufficiently large language models.

---

## Zero-shot CoT Prompting

Based on Kojima et al. (2022), this variation adds the phrase "Let's think step by step" without providing examples.

### Example Without Prompt Engineering

```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor
and 2 to the repairman. I then went and bought 5 more apples and ate 1.
How many apples did I remain with?
```

Output: 11 apples (incorrect)

### With "Let's think step by step"

```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor
and 2 to the repairman. I then went and bought 5 more apples and ate 1.
How many apples did I remain with?

Let's think step by step.
```

Output: Correct step-by-step reasoning yielding 10 apples.

This simple prompt is effective at this task and is particularly useful where you don't have too many examples.

---

## Automatic Chain-of-Thought (Auto-CoT)

Zhang et al. (2022) developed an automated method eliminating manual demonstration crafting. The approach uses language models with zero-shot CoT prompts to generate reasoning chains automatically.

### Two Stages

1. **Question Clustering**: Partition dataset questions into clusters
2. **Demonstration Sampling**: Select representative questions and generate reasoning chains using heuristics (e.g., 60-token length, 5 reasoning steps)

This automated approach maintains quality through diversity while reducing human effort.
