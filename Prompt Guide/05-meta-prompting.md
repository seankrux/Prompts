# Meta Prompting

Source: https://www.promptingguide.ai/techniques/meta-prompting

## Introduction

Meta Prompting represents an advanced technique emphasizing structural and syntactical aspects rather than specific content details. This methodology constructs abstract, structured interactions with large language models by prioritizing form and pattern over traditional content-centric methods.

## Key Characteristics

According to Zhang et al. (2024), meta prompting exhibits these defining traits:

1. **Structure-oriented**: Prioritizes the format and pattern of problems and solutions over specific content.

2. **Syntax-focused**: Employs syntax as a guiding template for expected responses or solutions.

3. **Abstract examples**: Uses abstracted frameworks illustrating problem/solution structures without focusing on specifics.

4. **Versatile**: Applicable across various domains for structured responses to diverse problems.

5. **Categorical approach**: Draws from type theory to emphasize categorization and logical arrangement of prompt components.

## Advantages over Few-Shot Prompting

Meta prompting and few-shot prompting differ fundamentally: meta prompting adopts a structure-oriented approach versus few-shot's content-driven emphasis.

Key advantages include:

1. **Token efficiency**: Reduces the number of tokens required by focusing on structure rather than detailed content.

2. **Fair comparison**: Provides equitable model comparison by minimizing specific example influence.

3. **Zero-shot efficacy**: Functions as zero-shot prompting with minimal example influence.

## Applications

Meta prompting leverages structural problem-solving patterns to enhance LLM reasoning capabilities across domains. However, effectiveness assumes the LLM possesses innate knowledge about the addressed task. Performance may deteriorate with novel, unique tasks -- similar to zero-shot limitations.

Beneficial applications include complex reasoning, mathematical problems, coding challenges, and theoretical queries.
