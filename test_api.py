#!/usr/bin/env python3
"""
Test script for the DeepSeek API client
"""

from api_client import DeepSeekAPIClient
import os

def test_api_client():
    """Test the API client functionality"""
    print("🤖 Testing DeepSeek API Client")
    print("=" * 40)
    
    # Initialize client
    client = DeepSeekAPIClient()
    
    # Check API key
    if not client.api_key:
        print("❌ API key not found in environment variables")
        return False
    
    print(f"✅ API key configured: {client.api_key[:10]}...")
    
    # Test simple code generation
    test_cases = [
        ("Python", "Create a function to calculate factorial"),
        ("JavaScript", "Create a function to validate email"),
        ("Java", "Create a simple Person class"),
    ]
    
    for language, prompt in test_cases:
        print(f"\n🔄 Testing {language} code generation...")
        print(f"Prompt: {prompt}")
        
        try:
            result = client.generate_code(prompt, language)
            if result and "Error:" not in result:
                print(f"✅ {language} generation successful")
                print(f"Generated {len(result)} characters of code")
            else:
                print(f"❌ {language} generation failed: {result}")
        except Exception as e:
            print(f"❌ {language} generation error: {str(e)}")
    
    print("\n🎉 API client testing completed!")

if __name__ == "__main__":
    test_api_client()
