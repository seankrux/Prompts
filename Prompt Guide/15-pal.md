# Program-Aided Language Models (PAL)

Source: https://www.promptingguide.ai/techniques/pal

## Overview

PAL (Program-Aided Language Models) represents a methodology where language models interpret natural language problems and generate programs as intermediate reasoning steps. Unlike chain-of-thought prompting which uses free-form text solutions, this approach delegates computational work to a programmatic runtime like Python.

The method, introduced by Gao et al. (2022), offloads solution steps to a programmatic interpreter rather than relying solely on textual reasoning.

## Implementation Example

### Setup Requirements

```python
import openai
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
```

### Configuration

```python
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model_name='text-davinci-003', temperature=0)
```

### Example Question

**Question:** "Today is 27 February 2023. I was born exactly 25 years ago. What is the date I was born in MM/DD/YYYY?"

The prompt includes several exemplars demonstrating how to structure date-related problems programmatically, showing the model the expected output format using Python's datetime operations.

### Model Output

The model generates:
```python
today = datetime(2023, 2, 27)
born = today - relativedelta(years=25)
born.strftime('%m/%d/%Y')
```

Executing this code produces: `02/27/1998`

## Workflow Summary

1. Provide few-shot examples in the prompt
2. Model generates Python code as reasoning steps
3. Execute generated code using `exec()`
4. Return the computational result
