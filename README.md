# Setup and Installation

## 1. Install Ollama according to your OS <br>
(a) For macOS 
``` 
curl -fsSL https://ollama.com/install.sh | sh
```
(b) For Ubuntu/ Linux
```
curl -fsSL https://ollama.com/install.sh | sh
```
(b) For Windows
```
irm https://ollama.com/install.ps1 | iex
```

## 2. Install Python
Install python, for Linux use the below commands:
```
sudo apt update
sudo apt install python3
python3 --version
```

## 3. Install VS code (Optional)
Install the VS code for writing and editing code. Its optional, you can use notepad or any word editor to write python code.

## 4. Installing required libraries
Install the required libraries and framework in virtual environment
```
python -m venv venv
source venv/bin/activate
pip install strands-agents
pip install strands-agents-tools
```

## 5. Final Step
Change the directory to venv and clone the code
```
cd venv/
git clone https://github.com/12345ujjwal/AI-agents.git
```
Run the code, (for example weather-agent.py)
```
python3 weather-agent.py
```
