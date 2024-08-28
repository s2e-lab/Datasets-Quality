# Datasets-Quality

This project contains source code for the paper "The Fault in our Stars: Quality Assessment of Code
Generation Benchmarks" published to the 24th IEEE International Conference on Source Code Analysis and Manipulation (SCAM 2024).

## Abstract
Large Language Models (e.g., GitHub Copilot, Chat-GPT, etc.) are gaining popularity among software engineers' daily practices. Developers are making conversations with the ChatGPT and share these conversations with their peers. A crucial aspect of developing effective code-generation LLMs is to evaluate these models using a robust dataset. Evaluation datasets with quality issues can provide a false sense of performance. In this work, we conduct the first-of-its-kind study of the quality of evaluation datasets used to benchmark different code generation models and developers’ prompts used to make conversation with models. To conduct this study, we manually analyzed 371 prompts from the developers and 3,566 prompts from 9 evaluation datasets to identify quality issues in them. We also empirically studied the effect of fixing the identified quality issues in the dataset and their correlation with the model’s performance. Finally, we investigated the memorization issues of the evaluation dataset, which can question the benchmark’s trustworthiness. We found that code generation evaluation benchmarks mainly focused on Python and coding exercises and had very limited contextual dependencies to challenge the model. These datasets and the developers’ prompts suffer from quality issues like spelling and grammatical errors, unclear intentions, and not using proper documentation style. Fixing all these issues in the benchmarks can lead to a better performance for Python code generation but not a significant improvement for Java code generation. We also found that GPT-3.5-Turbo and CodeGen-2.5 models possibly have data contamination issues.

## Folder Structure

- datasets, Combined_Datasets, Cleared_Datasets: contains the dataset used in the paper.
- Generation: contains the code used to generate the output of the model from the Cleared_Datasets.
- scripts: contains the scripts used to automatically marked the issues in the datasets.
- Automated_Analysis_Results: contains the results of the automated analysis of the datasets using the code from the scripts folder.
- Code_Clone_Results: contains the results of the code clone detection tools.





