# AI Agent

A command-line AI assistant powered by a local LLM via Ollama.

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.ai/) running locally

## Setup

1. **Install Ollama and pull a model:**
   ```bash
   ollama pull llama3.2:3b
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Ollama is running:**
   ```bash
   ollama serve
   ```

## Usage

```bash
python agent.py
```

The agent starts an interactive chat session. Type `exit`, `quit`, or `bye` to end.

## Configuration

| Setting | Location | Default |
|---------|----------|---------|
| Model | `agent.py` | `llama3.2:3b` |
| System prompt | `agent.py` | Customizable per use case |
| API endpoint | `agent.py` | `http://localhost:11434/v1` |

Swap models by changing the `model` parameter and customize the system prompt to tailor the agent's behavior for your specific use case.
