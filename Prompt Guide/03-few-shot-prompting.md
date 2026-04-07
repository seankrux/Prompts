# Few-Shot Prompting

Source: https://www.promptingguide.ai/techniques/fewshot

## Overview

Large language models demonstrate strong zero-shot capabilities but struggle with complex tasks in zero-shot settings. Few-shot prompting enables in-context learning by providing demonstrations that condition the model toward better performance. Research by Touvron et al. (2023) indicates these properties emerged when models reached sufficient scale.

## Core Concept

The technique works by showing the model examples of the desired task before requesting a response.

### Example: Learning a New Word

A classic demonstration from Brown et al. (2020) illustrates learning a new word's usage:

**Prompt:**
```
A "whatpu" is a small, furry animal native to Tanzania. An example
of a sentence that uses the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.

To do a "farduddle" means to jump up and down really fast. An
example of a sentence that uses the word farduddle is:
```

**Model Output:**
```
When we won the game, we all started to farduddle in celebration.
```

Models learn tasks from single examples (1-shot) and improve with increased demonstrations (3-shot, 5-shot, 10-shot).

## Key Findings from Min et al. (2022)

Research highlights important factors for effective demonstrations:

- Label space and input text distribution matter significantly, even with incorrect labels
- Format consistency improves performance substantially
- Random labels from true distributions outperform uniform distributions

## Format Flexibility

Models show robustness across inconsistent formats. Examples demonstrate correct predictions despite randomized or misaligned label placement, suggesting modern GPT models tolerate format variations better than previously expected.

## Limitations of Few-Shot Prompting

Standard few-shot prompting fails on complex reasoning tasks. Consider this arithmetic problem:

```
The odd numbers in this group add up to an even number:
15, 32, 5, 13, 82, 7, 1.
A:
```

Zero-shot outputs incorrectly claim these sum to 107 (an even number). Even with multiple training examples, few-shot prompting produces unreliable results for such reasoning tasks.

**Why it fails:** Complex arithmetic and symbolic reasoning require step-by-step problem decomposition rather than pattern matching from examples.

## Recommendations

When zero-shot and few-shot approaches prove insufficient, consider:

- Chain-of-thought prompting for reasoning tasks
- Fine-tuning models on domain-specific data
- Advanced prompting techniques addressing task complexity
