import requests
import os
from dotenv import load_dotenv
import json
import streamlit as st

load_dotenv()

class DeepSeekAPIClient:
    def __init__(self):
        """Initialize the DeepSeek API client with secure API key handling"""
        self.api_key = self._get_api_key()
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "deepseek/deepseek-r1-distill-llama-70b"
        
        # Debug info (without exposing the actual key)
        if self.api_key:
            print(f"✅ API Key loaded successfully: ...{self.api_key[-10:]}")
        else:
            print("❌ API Key not found")
    
    def _get_api_key(self) -> str:
        """Securely get API key from multiple sources with priority order"""
        
        # Priority 1: Streamlit Secrets (for Streamlit Cloud deployment)
        try:
            if hasattr(st, 'secrets') and 'OPENROUTER_API_KEY' in st.secrets:
                return st.secrets['OPENROUTER_API_KEY']
        except Exception:
            pass
        
        # Priority 2: Environment Variables (for GitHub Actions, Heroku, etc.)
        api_key = os.getenv('OPENROUTER_API_KEY')
        if api_key:
            return api_key
        
        # Priority 3: Local .env file (for local development only)
        try:
            load_dotenv(override=True)
            api_key = os.getenv('OPENROUTER_API_KEY')
            if api_key:
                return api_key
        except Exception:
            pass
        
        # Priority 4: Direct file reading as last resort
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('OPENROUTER_API_KEY='):
                        return line.split('=', 1)[1].strip().strip('"\'')
        except FileNotFoundError:
            pass
        except Exception:
            pass
        
        return None
        
    def generate_code(self, prompt, language):
        """Generate code using DeepSeek API through OpenRouter"""
        
        # Language-specific prompts to ensure proper code generation
        language_prompts = {
            "Python": f"Generate clean, well-documented Python code for the following request: {prompt}. Include comments and follow Python best practices.",
            "JavaScript": f"Generate clean, modern JavaScript code for the following request: {prompt}. Use ES6+ features and include comments.",
            "Java": f"Generate clean, well-structured Java code for the following request: {prompt}. Include proper class structure and comments.",
            "C++": f"Generate clean, efficient C++ code for the following request: {prompt}. Include proper headers and comments.",
            "Go": f"Generate clean, idiomatic Go code for the following request: {prompt}. Follow Go conventions and include comments."
        }
        
        full_prompt = language_prompts.get(language, f"Generate {language} code for: {prompt}")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "AI Code Generator"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": f"You are an expert {language} programmer. Generate clean, well-documented, and functional code. Only return the code without explanations unless specifically asked."
                },
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            "max_tokens": 2000,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    generated_code = result['choices'][0]['message']['content']
                    return self._clean_code_response(generated_code)
                else:
                    return "Error: No response generated"
            else:
                return f"Error: API request failed with status {response.status_code}: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"Error: Request failed - {str(e)}"
        except json.JSONDecodeError as e:
            return f"Error: Invalid JSON response - {str(e)}"
        except Exception as e:
            return f"Error: Unexpected error - {str(e)}"
    
    def _clean_code_response(self, response):
        """Clean the API response to extract just the code"""
        # Remove common markdown code block markers
        response = response.strip()
        
        # Remove code block markers
        if response.startswith('```'):
            lines = response.split('\n')
            # Remove first line (```language)
            lines = lines[1:]
            # Remove last line if it's just ```
            if lines and lines[-1].strip() == '```':
                lines = lines[:-1]
            response = '\n'.join(lines)
        
        return response.strip()
