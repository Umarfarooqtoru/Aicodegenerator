# AI Code Generator with DeepSeek API

This project is a Python Flask + Streamlit application that uses the DeepSeek API through OpenRouter to generate code in multiple programming languages with live preview functionality.

## 🚀 Features

- **AI-powered code generation** using DeepSeek R1 model
- **Support for 5 programming languages**: Python, JavaScript, Java, C++, Go
- **Real-time code preview** with syntax highlighting
- **Modern Streamlit UI** with responsive design
- **Flask backend** for API handling
- **Download functionality** for generated code
- **Copy to clipboard** feature

## 📋 Prerequisites

- Python 3.8 or higher
- OpenRouter API key for DeepSeek access

## 🛠️ Setup

### 1. Local Development Setup

1. **Clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/ai-code-generator.git
cd ai-code-generator
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure API Key** (Choose one method):

   **Method A: Environment File (Recommended for local development)**
   ```bash
   # Create .env file
   echo "OPENROUTER_API_KEY=your_openrouter_api_key_here" > .env
   ```

   **Method B: Environment Variable**
   ```bash
   # Windows
   set OPENROUTER_API_KEY=your_openrouter_api_key_here
   
   # Linux/Mac
   export OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

4. **Run the application**:
```bash
streamlit run app.py
```

### 2. Secure Deployment

For production deployments, use platform-specific secure methods:

- **Streamlit Cloud**: Add to app secrets in dashboard
- **GitHub Actions**: Add to repository secrets
- **Heroku**: Use `heroku config:set`
- **Railway/Render**: Add environment variables in dashboard

See `DEPLOYMENT_SECURITY_GUIDE.md` for detailed instructions.

## 🔐 Security

- ✅ **API keys are never stored in code**
- ✅ **Secure environment variable handling**
- ✅ **Automatic exclusion from Git**
- ✅ **Multiple deployment platform support**

**Important**: Never commit your `.env` file or actual API keys to Git!

## 🎯 Usage

1. **Select Programming Language**: Choose from Python, JavaScript, Java, C++, or Go
2. **Enter Prompt**: Describe what you want the code to do
3. **Generate Code**: Click the "Generate Code" button
4. **Review & Use**: View the generated code with syntax highlighting
5. **Download or Copy**: Save the code to your computer or copy to clipboard

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── api_client.py          # DeepSeek API client
├── flask_app.py           # Flask API server (optional)
├── test_api.py            # API testing script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── README.md              # This file
├── .github/
│   └── copilot-instructions.md
├── .vscode/
│   ├── tasks.json         # VS Code tasks
│   └── launch.json        # Debug configurations
└── .venv/                 # Virtual environment
```

## 🧪 Testing

Run the API test script to verify your setup:
```bash
python test_api.py
```

## 🎨 VS Code Integration

This project includes VS Code configurations for easy development:

- **Tasks**: Run Streamlit app, Flask API, or install dependencies
- **Launch configurations**: Debug the applications
- **Python environment**: Configured virtual environment

### Available VS Code Tasks:
- `Run Streamlit App`: Start the main Streamlit application
- `Run Flask API`: Start the Flask API server
- `Install Dependencies`: Install required Python packages

## 🔧 Configuration

### Supported Languages
- **Python**: General purpose programming
- **JavaScript**: Web development and Node.js
- **Java**: Enterprise and Android development
- **C++**: System programming and performance-critical applications
- **Go**: Cloud and microservices development

### API Configuration
- **Model**: DeepSeek R1 Distill Llama 70B
- **Provider**: OpenRouter
- **Timeout**: 30 seconds
- **Max tokens**: 2000

## 🛡️ Security

- API keys are stored in environment variables
- User inputs are validated
- Generated code is sanitized for display
- HTTPS is used for all API calls

## 🐛 Troubleshooting

1. **API Key Issues**: Ensure your OpenRouter API key is correctly set in the `.env` file
2. **Import Errors**: Make sure all dependencies are installed: `pip install -r requirements.txt`
3. **Port Conflicts**: Streamlit runs on port 8501 by default
4. **Network Issues**: Check your internet connection for API calls

## 📝 Example Prompts

### Python
- "Create a function to calculate fibonacci numbers"
- "Write a class for managing a todo list"
- "Implement a binary search algorithm"

### JavaScript
- "Create a React component for a user profile card"
- "Write an async function to fetch data from an API"
- "Implement a shopping cart with local storage"

### Java
- "Create a Student class with getters and setters"
- "Implement a simple calculator class"
- "Write a method to sort an array of integers"

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.
