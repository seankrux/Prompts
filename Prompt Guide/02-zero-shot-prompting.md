# Zero-Shot Prompting

Source: https://www.promptingguide.ai/techniques/zeroshot

Large language models (LLMs) today, such as GPT-3.5 Turbo, GPT-4, and Claude 3, are tuned to follow instructions and are trained on large amounts of data. Large-scale training makes these models capable of performing some tasks in a "zero-shot" manner. Zero-shot prompting means that the prompt used to interact with the model won't contain examples or demonstrations. The zero-shot prompt directly instructs the model to perform a task without any additional examples to steer it.

## Example

**Prompt:**
```
Classify the text into neutral, negative or positive.

Text: I think the vacation is okay.
Sentiment:
```

**Output:**
```
Neutral
```

Note that in the prompt above we didn't provide the model with any examples of text alongside their classifications, the LLM already understands "sentiment" -- that's the zero-shot capabilities at work.

## How It Works

Instruction tuning has been shown to improve zero-shot learning. Instruction tuning is essentially the concept of finetuning models on datasets described via instructions. Furthermore, RLHF (reinforcement learning from human feedback) has been adopted to scale instruction tuning wherein the model is aligned to better fit human preferences. This recent development powers models like ChatGPT.

## When Zero-Shot Fails

When zero-shot doesn't work, it's recommended to provide demonstrations or examples in the prompt which leads to few-shot prompting.
