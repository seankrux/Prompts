# Generated Knowledge Prompting

Source: https://www.promptingguide.ai/techniques/knowledge

## Overview

Generated Knowledge Prompting is a technique where language models generate relevant information before making predictions. According to research by Liu et al. 2022, this approach helps improve model performance on tasks requiring world knowledge, such as commonsense reasoning.

## Problem & Solution

**The Challenge:**
When asked "Part of golf is trying to get a higher point total than others. Yes or No?", an LLM initially responded with "Yes" -- an incorrect answer that reveals knowledge limitations.

**The Approach:**
The technique involves two stages:

1. **Knowledge Generation**: First, prompt the model to generate relevant factual information about the topic
2. **Informed Prediction**: Then, provide that generated knowledge alongside the original question to guide the model toward accurate answers

## Example Demonstration

The paper shows few-shot examples establishing the pattern:

- Input statements paired with factual knowledge (Greece vs. Mexico sizes, fog on glasses, fish cognition, smoking risks, rock definitions)
- For the golf question, the model generates two knowledge variants

**Generated Knowledge Sample:**
The model produced information stating that "The objective of golf is to play a set of holes in the least number of strokes" and that "The player with the lowest score wins."

## Results

When knowledge was integrated into the prompt:

- **Answer 1**: Model confidently responded "No" based on stroke-count knowledge
- **Answer 2**: Model showed less certainty using alternative phrasing about lowest scores

This demonstrates how generated context shifts model reasoning toward factually grounded responses.
