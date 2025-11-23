#!/bin/bash
# AI Content Explainer - Complete Startup Script

set -e  # Exit on error

echo "🚀 AI Content Explainer - Complete Setup & Start"
echo "================================================"
echo ""

# Check if we're in the right directory
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo "❌ Error: Please run this script from the learn-ai directory"
    exit 1
fi

# ============================================
# STEP 1: Backend Setup
# ============================================
echo "📦 STEP 1: Setting up Backend..."
echo ""

cd backend

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: You need to add your API key to backend/.env"
    echo "   Edit backend/.env and add ONE of these:"
    echo "   - ANTHROPIC_API_KEY=sk-ant-your-key-here  (Claude - you have this!)"
    echo "   - GEMINI_API_KEY=your-key-here            (Google - FREE)"
    echo "   - OPENAI_API_KEY=sk-your-key-here         (OpenAI)"
    echo ""
    echo "   Get keys from:"
    echo "   - Claude: https://console.anthropic.com/"
    echo "   - Gemini: https://aistudio.google.com/app/apikey"
    echo "   - OpenAI: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter after you've added your API key to backend/.env..."
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -q -r requirements.txt

echo "✅ Backend setup complete!"
echo ""

# ============================================
# STEP 2: Frontend Setup
# ============================================
echo "📦 STEP 2: Setting up Frontend..."
echo ""

cd ../frontend

# Install dependencies
if [ ! -d "node_modules" ]; then
    echo "Installing Node dependencies (this may take a minute)..."
    npm install
    echo "✅ Frontend dependencies installed!"
else
    echo "✅ Node modules already installed"
fi

echo ""

# ============================================
# STEP 3: Start Everything
# ============================================
echo "🚀 STEP 3: Starting servers..."
echo ""

# Start backend in background
echo "Starting backend server..."
cd ../backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
echo "Waiting for backend to start..."
sleep 5

# Start frontend
echo "Starting frontend server..."
cd ../frontend
npm start &
FRONTEND_PID=$!

# Wait a bit
sleep 3

echo ""
echo "=========================================="
echo "✅ AI Content Explainer is running!"
echo "=========================================="
echo ""
echo "🌐 Frontend: http://localhost:4200"
echo "🔧 Backend API: http://localhost:8000"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Wait for user to press Ctrl+C
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait
