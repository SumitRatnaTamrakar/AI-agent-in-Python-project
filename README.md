# AI Agent in Python

A command-line coding agent built in Python. It uses Google's Gemini API as the language model and a set of file and code-execution tools, so it can inspect a codebase, read and edit files, run Python scripts, and keep iterating on the results until a task is done.

This is a guided project from the [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python) course on Boot.dev.

## What it does

You give the agent a task in plain English. It decides which tools to call, runs them, reads the results, and repeats until it can give a final answer. The included `calculator` package is a small sample project the agent works on, for example to find and fix a bug.

## Features

- **Command-line interface:** pass a prompt as an argument and add `--verbose` to see the tool calls and their results.
- **Agentic loop:** the model and the tools exchange messages for up to 20 iterations, so the agent can act on what it learns at each step.
- **Four tools the agent can call:**
  - List files and directories
  - Read the contents of a file
  - Run a Python file
  - Write or overwrite a file
- **Function-calling layer:** `call_function.py` turns the model's tool requests into real function calls and returns the results to the model.
- **Configurable system prompt:** `prompts.py` tells the model how to plan and which tools it may use.
- **Test scripts:** one script per tool checks that it behaves as expected.

## Tech stack

- Python
- Google Gemini API (`google-genai`) with function calling
- `python-dotenv` for loading the API key
- [`uv`](https://docs.astral.sh/uv/) for dependency management

## Getting started

### Prerequisites

- Python (the version in `.python-version`)
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Installation

```bash
git clone https://github.com/SumitRatnaTamrakar/AI-agent-in-Python-project.git
cd AI-agent-in-Python-project
uv sync
```

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

Keep this file private. It is listed in `.gitignore` and should never be committed.

## Usage

```bash
uv run main.py "your prompt here"
```

Add `--verbose` to print the prompt, each tool call, and the tool results:

```bash
uv run main.py "Fix the bug in the calculator so that 3 + 7 * 2 gives the correct result" --verbose
```

<!-- VERIFY: replace the example prompt with one you actually ran -->

## How it works

1. `main.py` reads the prompt, loads the API key, and starts a conversation with the model.
2. The model replies with either a final answer or one or more tool calls.
3. `call_function.py` runs each requested tool and wraps the result as a message.
4. The tool results are appended to the conversation and sent back to the model.
5. The loop repeats (up to 20 times) until the model returns a final answer.

## Project structure

```
.
├── main.py                       # CLI entry point and the agent loop
├── call_function.py              # Dispatches tool calls from the model
├── prompts.py                    # System prompt
├── config.py                     # Configuration values
├── functions/                    # Tool implementations the agent can call
├── calculator/                   # Sample project the agent works on
├── test_get_files_info.py        # Tests for the directory listing tool
├── test_get_file_content.py      # Tests for the file reading tool
├── test_run_python_file.py       # Tests for the Python execution tool
├── test_write_file_content.py    # Tests for the file writing tool
├── pyproject.toml
└── uv.lock
```

## Running the tests

Each tool has its own test script:

```bash
uv run test_get_files_info.py
uv run test_get_file_content.py
uv run test_run_python_file.py
uv run test_write_file_content.py
```

## Safety note

This agent can write files and run Python code. Use it only on projects you trust, never on important code without a backup, and never share your API key.

## What I learned

- How tool calling and the agentic loop work with a pre-trained language model
- Designing small, well-defined functions that a model can call safely
- Writing a system prompt that guides the model's planning
- Handling API keys and configuration with environment variables
- Testing each tool independently of the model

## Acknowledgments

Built by following the guided project on [Boot.dev](https://www.boot.dev/courses/build-ai-agent-python).

## Author

**Sumit Ratna Tamrakar**, Computer Engineer focused on AI and machine learning.
[LinkedIn](https://www.linkedin.com/in/sumit-tamrakar) | [GitHub](https://github.com/SumitRatnaTamrakar)
