# Ollama Chat Interface Setup Guide

## Prerequisites Installation

### 1. Install Python

#### Windows:
1. Download Python from [python.org](https://python.org/downloads/)
2. Run the installer and **check "Add Python to PATH"**
3. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

#### macOS:
**Option 1 - Using Homebrew (Recommended):**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

**Option 2 - Direct Download:**
1. Download Python from [python.org](https://python.org/downloads/)
2. Run the installer
3. Verify installation:
   ```bash
   python3 --version
   pip3 --version
   ```

### 2. Install Ollama

#### Windows:
1. Download Ollama from [ollama.com](https://ollama.com/download)
2. Run the installer
3. Open Command Prompt and verify:
   ```cmd
   ollama --version
   ```

#### macOS:
**Option 1 - Using Homebrew:**
```bash
brew install ollama
```

**Option 2 - Direct Download:**
1. Download from [ollama.com](https://ollama.com/download)
2. Install the application
3. Verify installation:
   ```bash
   ollama --version
   ```

### 3. Install Ollama Models

After installing Ollama, you need to download at least one model:

```bash
# Download Llama 3.2 (3B parameters - recommended for most users)
ollama pull llama3.2

# Or download other models:
ollama pull llama3.2:1b    # Smaller, faster model
ollama pull codellama      # For code generation
ollama pull mistral        # Alternative model
```

Check available models:
```bash
ollama list
```

## Project Setup

### 1. Create Project Directory

#### Windows:
```cmd
mkdir ollama-chat-app
cd ollama-chat-app
```

#### macOS:
```bash
mkdir ollama-chat-app
cd ollama-chat-app
```

### 2. Create Virtual Environment

#### Windows:
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your command prompt
```

#### macOS:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

### 3. Install Dependencies

With your virtual environment activated:

#### Windows:
```cmd
pip install -r requirements.txt
```

#### macOS:
```bash
pip install -r requirements.txt
```

### 4. Create Application Files

Create two files in your project directory:

1. **requirements.txt** - (Use the content from the requirements.txt artifact above)
2. **app.py** - (Use the enhanced code from the Python artifact above)

### 5. Start Ollama Service

Before running the app, make sure Ollama is running:

#### Windows:
```cmd
ollama serve
```

#### macOS:
```bash
ollama serve
```

Leave this terminal open and open a new terminal for the next step.

### 6. Run the Application

With your virtual environment activated and Ollama running:

#### Windows:
```cmd
python app.py
```

#### macOS:
```bash
python app.py
```

The application will start and show:
```
Running on local URL:  http://127.0.0.1:7860
```

Open your web browser and go to `http://127.0.0.1:7860`

## Usage Instructions

1. **Select Model**: Choose from available models in the dropdown
2. **System Message**: Customize the AI's behavior and role
3. **Chat**: Type messages and get responses from your local AI
4. **Refresh Models**: Click to update the model list if you install new models
5. **Clear Chat**: Reset the conversation history

## Troubleshooting

### Common Issues:

1. **"ollama not found"**
   - Make sure Ollama is installed and in your PATH
   - Restart your terminal after installation

2. **"No models available"**
   - Install models using `ollama pull <model-name>`
   - Make sure Ollama service is running

3. **"Connection refused"**
   - Start Ollama service with `ollama serve`
   - Check if port 11434 is available

4. **Python/pip not found**
   - Reinstall Python and ensure "Add to PATH" is checked
   - Use `python3` and `pip3` on macOS if needed

### Deactivating Virtual Environment:
```bash
deactivate
```

### Reactivating Virtual Environment:

#### Windows:
```cmd
cd ollama-chat-app
venv\Scripts\activate
```

#### macOS:
```bash
cd ollama-chat-app
source venv/bin/activate
```

## Additional Features

The enhanced version includes:
- ✅ Multiple model support with dropdown selection
- ✅ Customizable system messages
- ✅ Model refresh functionality
- ✅ Better error handling
- ✅ Improved UI with better layout
- ✅ Clear chat functionality

## Next Steps

1. Try different models for different use cases
2. Experiment with system messages to change AI behavior
3. Consider adding more features like file upload or conversation saving
4. Explore other Ollama models for specialized tasks