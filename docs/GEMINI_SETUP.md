# Using Google Gemini API

The AI Content Explainer now supports **Google Gemini** as an AI provider!

## Why Gemini?

- ✅ **Free tier**: 15 requests per minute, 1 million tokens per day
- ✅ **Cost-effective**: Much cheaper than OpenAI for high volume
- ✅ **Fast**: Gemini 1.5 Flash is optimized for speed
- ✅ **Quality**: Similar quality to GPT-3.5 Turbo

## Getting Your Gemini API Key

1. Go to: **https://aistudio.google.com/app/apikey**
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

## Setup

### 1. Add to `.env` file:

```bash
cd backend
cp .env.example .env
# Edit .env and add:
GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start the server:

```bash
uvicorn main:app --reload
```

You should see:
```
✅ Google Gemini API key configured (AIzaSy...)
```

## Which AI Provider is Used?

The system tries AI providers in this order:

1. **Gemini** (if `GEMINI_API_KEY` is set) - FREE!
2. **OpenAI** (if `OPENAI_API_KEY` is set)
3. **Anthropic** (if `ANTHROPIC_API_KEY` is set)

**You only need ONE API key** - the system will automatically use whichever is available.

## Cost Comparison

| Provider | Model | Cost per 1M tokens (input) | Free Tier |
|----------|-------|---------------------------|-----------|
| **Gemini** | gemini-1.5-flash | $0.075 | ✅ 15 RPM, 1M tokens/day |
| OpenAI | gpt-3.5-turbo | $0.50 | ❌ None |
| OpenAI | gpt-4-turbo | $10.00 | ❌ None |
| Anthropic | claude-3-sonnet | $3.00 | ❌ None |

**For this app**: Average explanation = ~1500 tokens

- Gemini: **FREE** (within limits) or $0.0001 per explanation
- OpenAI GPT-4: $0.015 per explanation
- OpenAI GPT-3.5: $0.0008 per explanation

**Savings**: Using Gemini instead of GPT-4 = **99% cost reduction!**

## Example .env File

```bash
# Use ONLY ONE of these (Gemini recommended for free tier)
GEMINI_API_KEY=AIzaSyD...your...key...here

# Or use OpenAI
# OPENAI_API_KEY=sk-proj-...

# Or use Anthropic
# ANTHROPIC_API_KEY=sk-ant-...

# Rest of config
DATABASE_URL=sqlite:///./ai_explainer.db
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:4200,chrome-extension://*
```

## Testing

After setting up your Gemini key:

1. Start backend: `uvicorn main:app --reload`
2. Visit: http://localhost:8000/docs
3. Try the `/api/v1/explanation/example` endpoint
4. You should get an explanation powered by Gemini!

## Rate Limits

### Gemini Free Tier:
- 15 requests per minute
- 1 million tokens per day
- 1,500 requests per day

Our app's rate limiting (10 requests/hour) works perfectly within Gemini's limits.

### If You Hit Limits:

The app will show an error. Options:
1. Wait 1 minute (rate limit resets)
2. Upgrade to paid Gemini plan
3. Add OpenAI or Anthropic key as fallback

## Model Used

Currently using: **`gemini-1.5-flash`**

- Fastest Gemini model
- Best for real-time applications
- Great quality-to-speed ratio

Want to use a different model? Edit `backend/services/explanation_engine.py`:

```python
# Line 25
gemini_model = genai.GenerativeModel('gemini-1.5-pro')  # More powerful
# or
gemini_model = genai.GenerativeModel('gemini-1.0-pro')  # More stable
```

## Troubleshooting

### Error: "API key not valid"
- Check your key at https://aistudio.google.com/app/apikey
- Make sure it's in `.env` file as `GEMINI_API_KEY=...`
- Restart the backend server

### Error: "Resource exhausted"
- You've hit the free tier limit (15 requests/minute)
- Wait 1 minute and try again
- Or add another API key (OpenAI/Anthropic) as fallback

### Error: "No AI API key configured"
- Make sure `.env` file exists in `backend/` directory
- Check that `GEMINI_API_KEY` is uncommented
- Restart the server

## Benefits of Multi-Provider Support

Your app now supports 3 AI providers:

1. **Development**: Use free Gemini
2. **Production**: Scale with OpenAI/Anthropic
3. **Fallback**: If one provider is down, use another
4. **Cost optimization**: Use cheapest provider based on load

## Next Steps

1. ✅ Get your Gemini API key
2. ✅ Add to `.env` file
3. ✅ Run `pip install -r requirements.txt`
4. ✅ Start server and test!
5. 🎉 Enjoy free AI explanations!

---

**Pro tip**: Keep all three API keys configured for maximum reliability. The system will use Gemini first (free), then fallback to others if needed.
