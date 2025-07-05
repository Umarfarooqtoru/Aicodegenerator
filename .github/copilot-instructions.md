<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# AI Code Generator Project Instructions

This is a Python Flask + Streamlit application that integrates with the DeepSeek API through OpenRouter for AI-powered code generation.

## Project Context
- **Main Framework**: Streamlit for UI, Flask concepts for backend API handling
- **AI Provider**: DeepSeek R1 model via OpenRouter API
- **Supported Languages**: Python, JavaScript, Java, C++, Go
- **Key Features**: Code generation, live preview, syntax highlighting, download functionality

## Code Style Guidelines
- Follow PEP 8 for Python code
- Use clear, descriptive variable names
- Include comprehensive error handling
- Add docstrings for all functions and classes
- Use type hints where appropriate

## API Integration
- Use the OpenRouter API format for DeepSeek model calls
- Implement proper error handling for API requests
- Cache API client instances using Streamlit's caching mechanisms
- Handle rate limiting and timeouts gracefully

## UI/UX Guidelines
- Maintain responsive design using Streamlit columns
- Use consistent color scheme and styling
- Provide clear user feedback for all actions
- Include helpful tooltips and examples
- Ensure accessibility with proper labels and descriptions

## Security Considerations
- Keep API keys in environment variables
- Validate all user inputs
- Sanitize generated code display
- Use HTTPS for all API calls
