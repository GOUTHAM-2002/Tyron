from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import base64
import openai
from PIL import Image
from io import BytesIO
import uuid
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['GENERATED_FOLDER'] = 'generated_images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if avatar file was uploaded
        if 'avatar' not in request.files:
            return jsonify({'error': 'No avatar file uploaded'}), 400
        
        avatar_file = request.files['avatar']
        if avatar_file.filename == '':
            return jsonify({'error': 'No avatar file selected'}), 400
        
        if not allowed_file(avatar_file.filename):
            return jsonify({'error': 'Invalid file type. Please upload PNG, JPG, JPEG, or GIF'}), 400
        
        # Get prompts from form
        prompts = []
        for i in range(1, 6):
            prompt = request.form.get(f'prompt{i}', '').strip()
            if not prompt:
                return jsonify({'error': f'Prompt {i} is required'}), 400
            prompts.append(prompt)
        
        # Save avatar with unique filename
        avatar_filename = f"avatar_{uuid.uuid4().hex}.jpg"
        avatar_path = os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename)
        avatar_file.save(avatar_path)
        
        # Generate images
        generated_images = []
        for idx, prompt in enumerate(prompts, 1):
            print(f"Generating image {idx}...")
            
            # Generate image from prompt
            result = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            
            # Download and save the image
            image_url = result['data'][0]['url']
            response = requests.get(image_url)
            image_bytes = response.content
            image = Image.open(BytesIO(image_bytes))
            
            # Save with unique filename
            image_filename = f"story_image_{uuid.uuid4().hex}.jpg"
            image_path = os.path.join(app.config['GENERATED_FOLDER'], image_filename)
            image.save(image_path, format="JPEG", quality=90)
            
            generated_images.append({
                'filename': image_filename,
                'prompt': prompt,
                'index': idx
            })
        
        return jsonify({
            'success': True,
            'images': generated_images,
            'message': 'All 5 images generated successfully!'
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/generated_images/<filename>')
def generated_image(filename):
    return send_from_directory(app.config['GENERATED_FOLDER'], filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 