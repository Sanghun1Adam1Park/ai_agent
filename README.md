# ai_agent
Ai agent that will assist you coding using pre-trained LLM model 'gemini'
![Screenshot of AI Agent in action](https://raw.githubusercontent.com/Sanghun1Adam1Park/ai_agent/main/sc.png)


## Table of Contents
- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How to Use](#how-to-use)
- [Roadmap](#roadmap)
- [Acknowledgments](#acknowledgments)

## About The Project
This project is an AI agent designed to assist users in writing code within their codebase. It utilizes a pre-trained LLM model, `gemini`, to help with coding tasks. The agent operates by making a function call plan in response to user questions or requests, iteratively executing steps in an overall plan.

## Key Features
- **Code Assistance**: A helpful AI agent designed to assist with coding tasks within a codebase.
- **Function Call Planning**: Generates a plan of function calls based on user prompts.
- **Iterative Execution**: Operates in a loop, allowing for multiple function calls over successive turns to complete complex tasks.
- **File System Operations**:
  - Lists files and directories
  - Reads file contents
  - Executes Python files with optional arguments
  - Writes or overwrites files
- **Relative Path Handling**: All provided paths are relative to the working directory, which is automatically injected for security.
- **Initial Directory Scanning**: Most plans begin by scanning the working directory (`.`) for relevant files and directories.
- **Code Verification**: Executes both application code and tests after making modifications to ensure functionality.

## Built With
This project was built using the following technologies:
- Python3.10 >= 
- `google-genai==1.12.1`
- `python-dotenv==1.1.0`

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
Make sure you have Python 3 and pip installed on your system.

``` 
python --version
pip --version
```

### Installation 
1. Clone this repo.
```
git clone https://github.com/Sanghun1Adam1Park/ai_agent
```
2. Navigate to the project dir.
```
cd ai_agent
```

3. Installed the required dependencies. 
```
pip install -r requirements.txt
```

## How to use
Once installation is completed, you can run the agent from your terminal,
* Run with prompt:
```
python main.py "your prompt here"
```
* Run with a prompt and verbose output (to see token counts and function call details):
```
python main.py "your prompt here" --verbose
```
### Example
```
python main.py "How do I fix the calculator?"
```

## Roadmap

This is a list of proposed features and improvements for future versions of the agent:

* Fix harder and more complex bugs
* Refactor sections of code
* Add entirely new features
* Integrate with other LLM providers
* Explore other Gemini models
* Expand available functions for the agent
* Apply the agent to other codebases  
  *(remember to commit your changes before running the agent so you can always revert!)*

## Acknowledgments

* [Gemini Documentation](https://ai.google.dev/docs)
* [Boot.dev - Backend dev Tutorial](https://boot.dev)
