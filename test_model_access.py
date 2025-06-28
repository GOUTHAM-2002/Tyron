import os
from openai import OpenAI

# Load your OpenAI API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Testing OpenAI API access...")

# Test 1: Check available models
try:
    print("\n1. Checking available models...")
    models = client.models.list()
    image_models = [model.id for model in models.data if "image" in model.id.lower() or "dall" in model.id.lower()]
    print(f"Available image models: {image_models}")
except Exception as e:
    print(f"Error checking models: {e}")

# Test 2: Try a simple text completion to verify API key works
try:
    print("\n2. Testing basic API access...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello"}],
        max_tokens=10
    )
    print("✓ Basic API access works")
except Exception as e:
    print(f"✗ Basic API access failed: {e}")

# Test 3: Try GPT-Image-1 specifically
try:
    print("\n3. Testing GPT-Image-1 access...")
    # Try to get model info for gpt-image-1
    model_info = client.models.retrieve("gpt-image-1")
    print(f"✓ GPT-Image-1 model info: {model_info.id}")
except Exception as e:
    print(f"✗ GPT-Image-1 access failed: {e}")

print("\nTest completed. Check the results above.") 