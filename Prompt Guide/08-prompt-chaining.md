# Prompt Chaining

Source: https://www.promptingguide.ai/techniques/prompt_chaining

## Introduction

Breaking complex tasks into subtasks improves LLM performance and reliability. In prompt chaining, "a task is split into subtasks with the idea to create a chain of prompt operations." Each subtask's output feeds into the next prompt, creating sequential transformations.

## Advantages

This approach offers several advantages:

- Better performance on difficult tasks
- Improved transparency in LLM applications
- Increased controllability
- Easier debugging
- Enhanced reliability

It's particularly valuable for conversational assistants and personalized user experiences.

## Use Case: Document Question Answering

A practical example involves two-stage processing of document questions:

### Stage 1 - Extract Relevant Quotes

The first prompt identifies pertinent passages from source material based on the question. It uses placeholder syntax like `{{document}}` for flexibility. The system outputs extracted quotes in XML-style tags.

### Stage 2 - Generate Answer

The second prompt receives the extracted quotes plus the original document, synthesizing a helpful, accurate response with friendly tone.

## Key Benefits

- Transforms complex problems into manageable steps
- Enables debugging at each chain stage
- Increases application transparency and controllability
- Supports iterative improvement and analysis

Both steps can be tested using long-context models like Claude or GPT-4.
