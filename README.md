## An LLM Demo Using LangChain, Ollama and Chainlit
This is a basic local LLM demostration using the LangChain, Ollama, and Chainlit libraries. The LangChain chains the components of th>
## Installation
First install and run the Ollama server.
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then, create a ptyhon virtual environment (optional) and install the required libraries.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now, download your desired LLM from LLM community. You can use deepseek-coder for programming tasks.

**1.3B Parameter model** (Occupies about 5GB of VRAM)
```bash
ollama pull deepseek-coder
```

**7B Parameter model** (Occupies about 15GB of VRAM)
```bash
ollama pull deepseek-coder:6.7b
```

## Run the LLM Application
```bash
chainlit run chainlit-chat-ui.py
```