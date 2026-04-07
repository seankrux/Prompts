# Active-Prompt

Source: https://www.promptingguide.ai/techniques/activeprompt

## Overview

Active-Prompt is a prompting technique that addresses limitations in chain-of-thought (CoT) methods. Rather than relying on fixed human-annotated examples, this approach adapts language models to different task-specific prompts.

## The Problem

Traditional CoT methods depend on a predetermined set of human-annotated exemplars. These fixed examples may not be optimal for all task variations, potentially limiting model performance across different domains.

## The Solution

According to Diao et al. (2023), Active-Prompt works through an iterative selection process:

1. **Initial Query**: The LLM is queried with or without CoT examples
2. **Generate Responses**: The model produces k possible answers for training questions
3. **Measure Uncertainty**: An uncertainty metric (using disagreement) is calculated across the k answers
4. **Select Examples**: The most uncertain questions are identified for human annotation
5. **Refine and Infer**: New annotated exemplars are applied to answer each question

## Key Insight

By selectively identifying which training examples benefit most from human annotation, Active-Prompt makes the prompting process more efficient and effective. Rather than annotating all examples equally, resources focus on cases where model uncertainty is highest.
