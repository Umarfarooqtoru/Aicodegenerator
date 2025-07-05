from flask import Flask, request, jsonify
from api_client import DeepSeekAPIClient
import os

app = Flask(__name__)
api_client = DeepSeekAPIClient()

@app.route('/api/generate', methods=['POST'])
def generate_code():
    """Flask API endpoint for code generation"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        language = data.get('language', 'Python')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        generated_code = api_client.generate_code(prompt, language)
        
        return jsonify({
            'success': True,
            'code': generated_code,
            'language': language
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'AI Code Generator API'})

@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Get supported programming languages"""
    languages = ["Python", "JavaScript", "Java", "C++", "Go"]
    return jsonify({'languages': languages})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
