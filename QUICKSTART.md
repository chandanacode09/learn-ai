# Quick Start Guide

Get up and running in 5 minutes!

## Prerequisites

✅ Python 3.9+
✅ Node.js 18+
✅ OpenAI API key (get one at https://platform.openai.com/api-keys)

## Setup in 4 Steps

### 1️⃣ Backend Setup (2 minutes)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

**Edit `.env` and add your OpenAI API key:**
```
OPENAI_API_KEY=sk-your-key-here
```

**Start the backend:**
```bash
uvicorn main:app --reload
```

✅ Backend running at http://localhost:8000

### 2️⃣ Frontend Setup (2 minutes)

Open a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

✅ Frontend running at http://localhost:3000

### 3️⃣ Test It Out (30 seconds)

1. Open http://localhost:3000
2. Click "Try Example" button
3. See the explanation appear!

### 4️⃣ Chrome Extension (1 minute)

1. Open Chrome → `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the `extension` folder
5. Navigate to any article and click the extension icon!

## 🎉 You're Ready!

### Try These Next:

**Explain a URL:**
- Paste any article URL
- Choose explanation level (try ELI5!)
- Click "Explain Content"

**Explain GitHub Repo:**
- Switch to "GitHub" tab
- Enter `facebook/react` or any repo
- See architecture explained!

**Use the Extension:**
- Browse to any technical article
- Click extension icon
- Get instant summary!

## Troubleshooting

**Backend won't start?**
- Check you added your OpenAI API key to `.env`
- Make sure you're in the virtual environment

**Frontend won't connect?**
- Ensure backend is running on port 8000
- Check browser console for errors

**Extension not working?**
- Make sure backend is running
- Check extension has correct permissions
- Look at extension console (right-click → Inspect)

## What's Next?

- 📖 Read [SETUP.md](SETUP.md) for detailed configuration
- 🏗️ Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand the system
- 🚀 Check [README.md](README.md) for features and roadmap

## Need Help?

- Check API docs: http://localhost:8000/docs
- Review logs in terminal
- Check browser console (F12)

## Happy Explaining! 🧠
