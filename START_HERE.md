# 🚀 Quick Start - Actually Get it Running!

Follow these steps **exactly** to get the app working:

## Step 1: Get Your Claude API Key (1 minute)

Since you have a Claude API key:

1. Go to: https://console.anthropic.com/
2. Copy your API key (starts with `sk-ant-...`)

## Step 2: Add Your API Key (30 seconds)

```bash
cd backend
cp .env.example .env
```

Now edit `backend/.env` and change this line:
```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

To:
```bash
ANTHROPIC_API_KEY=sk-ant-YOUR-ACTUAL-KEY-HERE
```

Save the file.

## Step 3: Run the Startup Script (2 minutes)

```bash
cd /home/user/learn-ai
chmod +x start.sh
./start.sh
```

**OR** do it manually:

### Option A: Manual Start (Backend)

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start server
python -m uvicorn main:app --reload
```

You should see:
```
✅ Anthropic API key configured (sk-ant-...)
🌐 API running at http://localhost:8000
```

### Option B: Manual Start (Frontend)

Open a **new terminal**:

```bash
cd frontend
npm install
npm start
```

Angular will start on: http://localhost:4200

## Step 4: Test It! (30 seconds)

1. Open browser: http://localhost:4200
2. Click "Try Example" button
3. You should see an explanation appear!

---

## 🔧 Troubleshooting

### Error: "No AI API key configured"

**Fix**: You didn't add your Claude API key to `backend/.env`

```bash
# Edit this file
nano backend/.env

# Add your key
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

### Error: "Module not found"

**Fix**: Install dependencies

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "Port 8000 already in use"

**Fix**: Kill the process

```bash
lsof -ti:8000 | xargs kill -9
```

### Error: "npm: command not found"

**Fix**: Install Node.js

```bash
# Check if Node is installed
node --version

# If not, install it
# Ubuntu/Debian:
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Frontend won't start

**Fix**: Clear cache and reinstall

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

---

## 🎯 Quick Test Checklist

- [ ] Backend running on http://localhost:8000
- [ ] Visit http://localhost:8000/docs - you see API documentation
- [ ] Frontend running on http://localhost:4200
- [ ] Click "Try Example" button - you see an explanation

---

## 📝 What Should You See?

### Backend Terminal:
```
🚀 Starting AI Content Explainer API...
✅ Anthropic API key configured (sk-ant-...)
✅ Database initialized
✅ Caching enabled (24 hour TTL)
✅ Rate limiting: 10 requests/hour for free tier
🌐 API running at http://localhost:8000
📖 API docs at http://localhost:8000/docs
```

### Frontend Terminal:
```
** Angular Live Development Server is listening on localhost:4200 **
✔ Compiled successfully.
```

### Browser (http://localhost:4200):
You should see a clean interface with:
- Title: "AI Content Explainer"
- Input form with URL/Text/GitHub tabs
- "Try Example" button
- Click it and get an explanation!

---

## ❓ Still Not Working?

Tell me **exactly** what you see:

1. What command did you run?
2. What error message do you get?
3. Paste the terminal output

I'll help you fix it immediately!
