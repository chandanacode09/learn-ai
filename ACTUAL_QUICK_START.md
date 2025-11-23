# 🚀 ACTUALLY Start This Thing - 3 Commands Only

I'm sorry it's been confusing. Here's **exactly** what to do:

## Prerequisites
- Python 3.9+ installed
- Node.js 18+ installed
- Your Claude API key

---

## 🎯 Three Steps to Run It

### 1️⃣ Setup Backend (2 minutes)

```bash
cd /home/user/learn-ai/backend

# Create .env file
cat > .env << 'EOF'
ANTHROPIC_API_KEY=PUT_YOUR_CLAUDE_API_KEY_HERE
DATABASE_URL=sqlite:///./ai_explainer.db
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:4200,chrome-extension://*
EOF

# Create virtual environment & install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start server
python -m uvicorn main:app --reload
```

**Replace `PUT_YOUR_CLAUDE_API_KEY_HERE` with your actual key!**

Leave this terminal running. You should see:
```
✅ Anthropic API key configured
🌐 API running at http://localhost:8000
```

---

### 2️⃣ Setup Frontend (2 minutes)

Open a **NEW terminal**:

```bash
cd /home/user/learn-ai/frontend
npm install
npm start
```

This will open http://localhost:4200 automatically.

---

### 3️⃣ Test It (10 seconds)

1. Browser opens at http://localhost:4200
2. Click the **"Try Example"** button
3. You should see an AI explanation appear!

That's it! ✅

---

## 🐛 If Something Breaks

### "No API key configured"
Your `.env` file is wrong. Check:
```bash
cat backend/.env
```
Should show your actual Claude API key.

### "Module not found"
You didn't install dependencies:
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### "Port already in use"
Something is running on port 8000 or 4200:
```bash
# Kill port 8000
lsof -ti:8000 | xargs kill -9

# Kill port 4200
lsof -ti:4200 | xargs kill -9
```

### Still broken?
Run this and show me the output:
```bash
cd /home/user/learn-ai/backend
source venv/bin/activate
python -m uvicorn main:app --reload
```

---

## 📋 What You Should See

**Backend terminal:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
🚀 Starting AI Content Explainer API...
✅ Anthropic API key configured (sk-ant-...)
✅ Database initialized
✅ Caching enabled (24 hour TTL)
🌐 API running at http://localhost:8000
```

**Frontend terminal:**
```
** Angular Live Development Server is listening on localhost:4200 **
✔ Compiled successfully.
```

**Browser (http://localhost:4200):**
Nice interface with explanation form!

---

That's literally it. Two terminals, three commands, done. If this still doesn't work, copy/paste the exact error message and I'll fix it immediately.
