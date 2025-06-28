import os
from openai import OpenAI

# Load your OpenAI API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Checking GPT-Image-1 quota status...")

try:
    # Try to get model info to check access
    model_info = client.models.retrieve("gpt-image-1")
    print(f"✓ GPT-Image-1 model access: {model_info.id}")
    
    # Try a minimal GPT-Image-1 request to test quota
    print("\nTesting GPT-Image-1 quota...")
    result = client.images.edit(
        model="gpt-image-1",
        image=[open("avatar.jpg", "rb")],
        prompt="A simple test image",
        size="1024x1024"
    )
    print("✓ GPT-Image-1 quota test successful!")
    
except Exception as e:
    print(f"✗ GPT-Image-1 quota error: {e}")
    print("\nTo fix this:")
    print("1. Check your OpenAI account limits at platform.openai.com")
    print("2. Wait for quota reset (usually daily)")
    print("3. Contact OpenAI support if you have sufficient credits")
    print("4. Try creating a new API key")

print("\nQuota check completed.") 