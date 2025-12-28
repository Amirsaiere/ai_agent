# AI Coding Agent

A command-line AI agent that autonomously debugs and fixes Python code using the Gemini API and function calling.

## Overview

This project explores building an autonomous coding assistant similar to Claude Code. The agent accepts natural language coding tasks, selects appropriate tools from its function library, and iteratively works toward task completion.

### Example Usage
```sh
> uv run main.py "fix my calculator app, it's not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. 
# The output shows the expression and the result in a formatted way.
```

## Features

The agent can:
- **Scan directories** to understand project structure
- **Read file contents** to analyze code
- **Write/modify files** to implement fixes
- **Execute Python files** to test changes
- **Iterate autonomously** until task completion

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager ([installation docs](https://docs.astral.sh/uv/))
- Unix-like shell (zsh, bash)
- Gemini API key

## Installation
```sh
# Clone the repository
git clone <your-repo-url>
cd ai-coding-agent

# Install dependencies with uv
uv sync
```

## Configuration

Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the agent with a coding task:
```sh
uv run main.py "your task description here"
```

## Learning Goals

This project demonstrates:
1. **Multi-directory Python project structure** and organization
2. **LLM function calling** and agentic workflows
3. **API integration** with Gemini for autonomous task completion
4. **Functional programming** patterns in Python

## Technical Stack

- **LLM**: Google Gemini API
- **Language**: Python 3.10+
- **Package Manager**: uv
- **Architecture**: Function-calling agent with iterative execution

## Project Structure
```
ai-coding-agent/
├── main.py           # CLI entry point
├── agent/            # Agent logic and function definitions
├── tools/            # File system and execution tools
└── tests/            # Test cases and sample projects
```

## Limitations

- Currently supports Python file operations only
- Requires clear task descriptions for best results
- May require multiple iterations for complex tasks

## Future Improvements

- Add support for additional programming languages
- Implement memory/context management for longer sessions
- Expand tool library (git operations, testing, deployment)
