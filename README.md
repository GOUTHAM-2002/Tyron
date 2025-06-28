# AI Story Generator

A Flask web application that generates AI-powered story images based on user prompts and avatar uploads using OpenAI's image editing API.

## Features

- Upload avatar images (PNG, JPG, JPEG, GIF)
- Generate 5 unique story images using AI
- Modern, responsive web interface
- Real-time image generation with progress feedback

## Local Development

### Prerequisites

- Python 3.9 or higher
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd TyronZProject
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file or set environment variable
export OPENAI_API_KEY="your-openai-api-key-here"
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Deployment on Render

### Step 1: Prepare Your Repository

1. Make sure your code is in a Git repository (GitHub, GitLab, etc.)
2. Ensure all files are committed and pushed to your repository

### Step 2: Create a Render Account

1. Go to [render.com](https://render.com)
2. Sign up for a free account
3. Connect your GitHub/GitLab account

### Step 3: Deploy Your Application

1. **From Render Dashboard:**
   - Click "New +" button
   - Select "Web Service"
   - Connect your repository
   - Choose the repository containing your project

2. **Configure the Service:**
   - **Name:** `ai-story-generator` (or any name you prefer)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free

3. **Set Environment Variables:**
   - Click on "Environment" tab
   - Add the following environment variable:
     - **Key:** `OPENAI_API_KEY`
     - **Value:** Your actual OpenAI API key
     - **Sync:** Leave unchecked (for security)

4. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Step 4: Access Your Application

- Once deployment is complete, Render will provide you with a URL
- Your application will be available at: `https://your-app-name.onrender.com`

## Project Structure

```
TyronZProject/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── templates/
│   └── index.html       # Main web interface
├── uploads/             # User uploaded avatars (auto-created)
└── generated_images/    # AI-generated images (auto-created)
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## API Endpoints

- `GET /`: Main application page
- `POST /upload`: Upload avatar and generate images
- `GET /generated_images/<filename>`: Serve generated images
- `GET /uploads/<filename>`: Serve uploaded avatars

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI:** OpenAI GPT-4 Vision API
- **Image Processing:** Pillow (PIL)
- **Deployment:** Render

## Notes

- The free tier of Render has limitations on build time and monthly usage
- Generated images are stored locally and will be lost when the service restarts
- For production use, consider using cloud storage for images

## Troubleshooting

### Common Issues:

1. **Build fails:** Check that all dependencies are in `requirements.txt`
2. **Environment variables not working:** Ensure they're set correctly in Render dashboard
3. **Images not generating:** Verify your OpenAI API key is valid and has sufficient credits
4. **Service not starting:** Check the logs in Render dashboard for error messages

### Getting Help:

- Check Render's documentation: [docs.render.com](https://docs.render.com)
- Review the application logs in your Render dashboard
- Ensure your OpenAI API key has the necessary permissions

## License

This project is open source and available under the MIT License. 