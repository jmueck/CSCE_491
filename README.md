# CTF Dataset and RAG Experiment Repository

This repository contains datasets, tests, results, and scripts related to the Retrieval-Augmented Generation (RAG) system used to evaluate Large Language Models (LLMs) for solving Capture The Flag (CTF) challenges. The repository is organized as follows:

## Repository Structure

### 1. **CTF\_Dataset/**

- Contains subfolders with JSON files representing CTF problems used to populate the RAG database.

- Each JSON provides structured data for individual CTF challenges, formatted for efficient retrieval and querying by the RAG system.

- All CTF datasets were gathered from the Texas A&M Cybersecurity CTF Challenges Github Repositories which can be found here:\
  [https://github.com/tamuctf/TAMUctf-2024](https://github.com/tamuctf/TAMUctf-2024)

  [https://github.com/tamuctf/TAMUctf-2023](https://github.com/tamuctf/TAMUctf-2023)

  [https://github.com/tamuctf/TAMUctf-2022](https://github.com/tamuctf/TAMUctf-2022)

  [https://github.com/tamuctf/TAMUctf-2021](https://github.com/tamuctf/TAMUctf-2021)

  [https://github.com/tamuctf/TAMUctf-2020](https://github.com/tamuctf/TAMUctf-2020)

  [https://github.com/tamuctf/TAMUctf-2019](https://github.com/tamuctf/TAMUctf-2019)



### 2. **Problem Tests and Results/**

- Houses test data and results for three distinct categories of Pico CTF challenges:
  - **Binary Exploitation/**
  - **Cryptography/**
  - **Reverse Engineering/**
- Each category is further divided into difficulty levels:
  - **Easy/**
  - **Medium/**
  - **Hard/**
- Inside each difficulty subfolder:
  - **Any Source Code Files for the Problem (if available)**
  - **Chat History PDF**: PDF documenting the interaction between the LLM and the test problem. These interactions capture the process by which the LLM attempted to solve the problem.
- Source of PicoCTF Challenges:\
  [https://play.picoctf.org/practice](https://play.picoctf.org/practice)

### 3. **createJson.py**

- A Python script used to create the JSON files for the RAG database in the `CTF_Dataset/` folder.
- Includes functions for converting CTF problems into the appropriate format required for integration into the RAG system.

## Usage

### Preparing the Dataset

1. Used` createJson.py` to format new CTF problems into JSON files.
2. Added the generated JSONs to the appropriate subfolder in `CTF_Dataset/`.

### Examining Tests

1. Navigate to the `Problem Tests and Results/` directory.
2. Select the appropriate challenge category and difficulty level.
3. Review the problem definition and chat history to analyze the LLM’s performance.
