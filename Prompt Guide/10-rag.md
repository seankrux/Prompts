# Retrieval Augmented Generation (RAG)

Source: https://www.promptingguide.ai/techniques/rag

## Overview

General-purpose language models can be fine-tuned for tasks like sentiment analysis and named entity recognition. However, more complex, knowledge-intensive tasks benefit from systems that access external knowledge sources, improving factual consistency and reducing hallucinations.

Meta AI researchers developed Retrieval Augmented Generation (RAG) to address knowledge-intensive challenges. "RAG combines an information retrieval component with a text generator model" and can be efficiently modified without retraining the entire system.

## How RAG Works

The RAG process works by taking an input, retrieving relevant supporting documents from a source like Wikipedia, concatenating these documents as context with the original prompt, and feeding this combined input to a text generator for final output production.

Lewis et al. (2021) proposed a general-purpose fine-tuning approach using:
- A pre-trained seq2seq model as parametric memory
- A dense vector index of Wikipedia as non-parametric memory
- A neural pre-trained retriever for access

## Performance

RAG demonstrates strong performance on several benchmarks including Natural Questions, WebQuestions, and CuratedTrec. It generates more factual, specific, and diverse responses when tested on MS-MARCO and Jeopardy questions, plus improved results on FEVER fact verification.

Modern implementations combine retriever-based approaches with popular LLMs like ChatGPT to enhance capabilities and factual accuracy.

## RAG Use Case: Generating Friendly ML Paper Titles

A notebook tutorial demonstrates using open-source LLMs to build a RAG system for generating concise machine learning paper titles:
- https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-rag.ipynb

## References

- Retrieval-Augmented Generation for Large Language Models: A Survey (Dec 2023)
- Retrieval Augmented Generation: Streamlining the creation of intelligent natural language processing models (Sep 2020)
