#!/bin/bash
# Quick setup script for AI Content Explainer

set -e

echo "🔧 AI Content Explainer - Quick Setup"
echo "====================================="
echo ""

# Check if we're in the right place
if [ ! -f "backend/requirements.txt" ]; then
    echo "❌ Error: Run this from the learn-ai directory"
    exit 1
fi

# Setup backend
echo "📦 Setting up backend..."
cd backend

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit backend/.env and add your API key!"
    echo ""
    echo "You need ONE of these:"
    echo "  • ANTHROPIC_API_KEY=sk-ant-... (Claude)"
    echo "  • GEMINI_API_KEY=... (Google - FREE!)"
    echo "  • OPENAI_API_KEY=sk-... (OpenAI)"
    echo ""
    echo "Get keys from:"
    echo "  • Claude: https://console.anthropic.com/"
    echo "  • Gemini: https://aistudio.google.com/app/apikey"
    echo "  • OpenAI: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter after adding your API key to backend/.env..."
else
    echo "✓ .env file exists"
fi

# Create venv if needed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate and install
echo "Installing dependencies..."
source venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo "✅ Backend setup complete!"
cd ..

# Setup frontend
echo ""
echo "📦 Setting up frontend..."
cd frontend

if [ ! -d "node_modules" ]; then
    echo "Installing npm dependencies (this may take a minute)..."
    npm install
else
    echo "✓ npm dependencies already installed"
fi

echo "✅ Frontend setup complete!"
cd ..

echo ""
echo "========================================"
echo "✅ Setup complete!"
echo "========================================"
echo ""
echo "To start the app:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python -m uvicorn main:app --reload"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open: http://localhost:4200"
echo ""
