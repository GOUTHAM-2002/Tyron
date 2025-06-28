#!/usr/bin/env python3
"""
Test script to verify deployment compatibility
"""

def test_imports():
    """Test that all required packages can be imported"""
    try:
        import flask
        print("✓ Flask imported successfully")
        
        from openai import OpenAI
        print("✓ OpenAI imported successfully")
        
        from PIL import Image
        print("✓ Pillow imported successfully")
        
        import requests
        print("✓ Requests imported successfully")
        
        import gunicorn
        print("✓ Gunicorn imported successfully")
        
        print("\n🎉 All imports successful! Deployment should work.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_basic_functionality():
    """Test basic Flask app creation"""
    try:
        from flask import Flask
        app = Flask(__name__)
        print("✓ Flask app created successfully")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def test_openai_client():
    """Test OpenAI client creation"""
    try:
        from openai import OpenAI
        client = OpenAI(api_key="test-key")
        print("✓ OpenAI client created successfully")
        return True
    except Exception as e:
        print(f"❌ OpenAI client creation failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing deployment compatibility...\n")
    
    imports_ok = test_imports()
    flask_ok = test_basic_functionality()
    openai_ok = test_openai_client()
    
    if imports_ok and flask_ok and openai_ok:
        print("\n✅ All tests passed! Ready for deployment.")
    else:
        print("\n❌ Some tests failed. Check requirements.txt") 