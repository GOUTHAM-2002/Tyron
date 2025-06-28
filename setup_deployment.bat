@echo off
echo ========================================
echo AI Story Generator - Deployment Setup
echo ========================================
echo.

echo Step 1: Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/
    pause
    exit /b 1
)
echo Git is installed ✓
echo.

echo Step 2: Initializing Git repository...
if not exist ".git" (
    git init
    echo Git repository initialized ✓
) else (
    echo Git repository already exists ✓
)
echo.

echo Step 3: Adding files to Git...
git add .
echo Files added to Git ✓
echo.

echo Step 4: Making initial commit...
git commit -m "Initial commit - AI Story Generator"
echo Initial commit created ✓
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a GitHub repository at: https://github.com/new
echo 2. Name it: ai-story-generator
echo 3. Make it PUBLIC (required for Render free tier)
echo 4. Run these commands:
echo    git remote add origin https://github.com/YOUR_USERNAME/ai-story-generator.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 5. Then follow the deployment guide in deploy_guide.md
echo.
pause 