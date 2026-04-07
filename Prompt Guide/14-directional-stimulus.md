# Directional Stimulus Prompting

Source: https://www.promptingguide.ai/techniques/dsp

## Overview

Directional Stimulus Prompting is a prompting technique proposed by Li et al. (2023) designed to better guide language models in generating desired outputs, particularly for summarization tasks.

## Key Concept

The approach involves training a tunable policy language model to generate stimulus or hints. These hints guide a frozen, black-box LLM toward producing the target output. This represents an increased application of reinforcement learning for LLM optimization.

## How It Works

The policy LM can remain small while being specifically optimized to create hints that effectively direct a larger, frozen language model. The technique contrasts with standard prompting approaches by providing more targeted directional guidance.
