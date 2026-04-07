# ReAct Prompting

Source: https://www.promptingguide.ai/techniques/react

## Introduction

The ReAct framework, introduced by Yao et al. (2022), enables language models to generate both reasoning traces and task-specific actions in alternating sequences. This approach allows models to form, monitor, and revise action plans while handling unforeseen issues. The action component enables integration with external sources like knowledge bases or environments.

Research demonstrates that ReAct surpasses multiple benchmarks on language and decision-making tasks. It enhances human interpretability and trustworthiness. The most effective implementations combine ReAct with chain-of-thought methodology, leveraging both internal knowledge and external information gathered during reasoning.

## How It Works

ReAct draws inspiration from how humans combine acting and reasoning to acquire new capabilities and make informed decisions.

Chain-of-thought prompting has demonstrated that models can generate reasoning sequences for arithmetic and commonsense problems. However, the inability to access external information or refresh knowledge creates problems including factual inaccuracies and cascading errors.

ReAct merges reasoning and action processes with language models. The system generates verbal reasoning traces alongside actions, enabling dynamic thought processes to create, sustain, and modify plans while interfacing with external sources (such as Wikipedia) to incorporate new information.

## ReAct Prompting Structure

Training exemplars combine multiple thought-action-observation sequences:

```
Question: What is the elevation range for the area that the eastern
sector of the Colorado orogeny extends into?

Thought 1: I need to search Colorado orogeny, find the area that the
eastern sector of the Colorado orogeny extends into, then find the
elevation range of the area.

Action 1: Search[Colorado orogeny]

Observation 1: The Colorado orogeny was an episode of mountain building
(an orogeny) in Colorado and surrounding areas.

Thought 2: It does not mention the eastern sector. So I need to look up
eastern sector.

Action 2: Lookup[eastern sector]

Observation 2: (Result 1 / 1) The eastern sector extends into the High
Plains and is called the Central Plains orogeny.

Thought 3: The eastern sector of Colorado orogeny extends into the High
Plains. So I need to search High Plains and find its elevation range.

Action 3: Search[High Plains]

Observation 3: High Plains refers to one of two distinct land regions

Thought 4: I need to instead search High Plains (United States).

Action 4: Search[High Plains (United States)]

Observation 4: The High Plains are a subregion of the Great Plains. From
east to west, the High Plains rise in elevation from around 1,800 to
7,000 ft (550 to 2,130 m).

Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft,
so the answer is 1,800 to 7,000 ft.

Action 5: Finish[1,800 to 7,000 ft]
```

### Task-Specific Approaches

- **Reasoning-heavy tasks** (HotpotQA): Multiple thought-action-observation cycles
- **Action-heavy tasks**: Sparse thoughts with frequent actions

## Results on Knowledge-Intensive Tasks

Performance evaluation using PaLM-540B on HotPotQA and Fever datasets shows:

- ReAct outperforms action-only approaches on both benchmarks
- ReAct exceeds CoT on Fever; CoT leads on HotpotQA
- Combined ReAct + CoT with self-consistency surpasses individual methods

**Key Findings:**
- CoT experiences factual hallucination issues
- ReAct's structural design limits reasoning flexibility
- ReAct depends heavily on retrieval quality; poor search results disrupt reasoning recovery

## Results on Decision Making Tasks

Evaluation on ALFWorld (text-based gaming) and WebShop (e-commerce simulation):

ReAct demonstrates superior performance compared to action-only approaches on both environments. Without reasoning, action-only methods struggle decomposing objectives into manageable subgoals. However, prompting-based systems still lag substantially behind expert human performance on these complex tasks.

## LangChain ReAct Usage

### Setup

```python
import openai
import os
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
```

### Agent Configuration

```python
llm = OpenAI(model_name="text-davinci-003", temperature=0)
tools = load_tools(["google-serper", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
```

### Query Execution

```python
agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")
```

### Execution Output

```
> Entering new AgentExecutor chain...
 I need to find out who Olivia Wilde's boyfriend is and then calculate
his age raised to the 0.23 power.

Action: Search
Action Input: "Olivia Wilde boyfriend"
Observation: Olivia Wilde started dating Harry Styles after ending her
years-long engagement to Jason Sudeikis.

Thought: I need to find out Harry Styles' age.
Action: Search
Action Input: "Harry Styles age"
Observation: 29 years

Thought: I need to calculate 29 raised to the 0.23 power.
Action: Calculator
Action Input: 29^0.23
Observation: Answer: 2.169459462491557

Thought: I now know the final answer.
Final Answer: Harry Styles, Olivia Wilde's boyfriend, is 29 years old
and his age raised to the 0.23 power is 2.169459462491557.

> Finished chain.
```
