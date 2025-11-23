# AI Content Explainer - Setup Guide

Complete setup guide for development and deployment.

## Prerequisites

- Python 3.9+
- Node.js 18+
- npm or yarn
- Chrome browser (for extension)
- Git

## Environment Setup

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd learn-ai
```

### 2. Backend Setup

#### Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Configure Environment

Create `.env` file from example:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
OPENAI_API_KEY=sk-...your-key...
# OR
ANTHROPIC_API_KEY=sk-ant-...your-key...
```

**Required API Keys:**
- **OpenAI**: Get from https://platform.openai.com/api-keys
- **Anthropic** (optional): Get from https://console.anthropic.com/

#### Run Backend Server

```bash
# From backend directory
uvicorn main:app --reload

# Server will start at http://localhost:8000
# API docs available at http://localhost:8000/docs
```

### 3. Frontend Setup

#### Install Dependencies

```bash
cd ../frontend
npm install
```

#### Configure Environment

Create `.env.local`:

```bash
cp .env.local.example .env.local
```

Default configuration points to `http://localhost:8000` - update if needed.

#### Run Development Server

```bash
npm run dev

# Server will start at http://localhost:3000
```

### 4. Chrome Extension Setup

#### Load Extension

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top right)
3. Click "Load unpacked"
4. Select the `extension` directory from this project
5. Extension icon should appear in your toolbar

#### Configure Extension

The extension is pre-configured to connect to:
- Backend API: `http://localhost:8000`
- Web App: `http://localhost:3000`

To change these, edit `extension/popup.js`.

## Verification

### Test Backend

```bash
curl http://localhost:8000/api/v1/health
# Should return: {"status":"healthy"...}
```

Or visit http://localhost:8000/docs for interactive API documentation.

### Test Frontend

1. Open http://localhost:3000
2. You should see the AI Content Explainer homepage
3. Try the "Try Example" button

### Test Extension

1. Click the extension icon
2. Navigate to any article (e.g., a Medium or Dev.to post)
3. Click "Explain This Page"
4. You should see a summary within seconds

## Troubleshooting

### Backend Issues

**Error: No API key found**
- Make sure you've created `.env` file in `backend/` directory
- Add either `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`

**Error: Module not found**
- Run `pip install -r requirements.txt` again
- Make sure you're in the virtual environment

**CORS errors**
- Check that frontend URL is in `CORS_ORIGINS` in config
- Default includes `http://localhost:3000`

### Frontend Issues

**Error: Cannot connect to API**
- Make sure backend is running on http://localhost:8000
- Check `NEXT_PUBLIC_API_URL` in `.env.local`

**Dependencies installation fails**
- Try deleting `node_modules` and `package-lock.json`
- Run `npm install` again

### Extension Issues

**Extension not loading**
- Make sure you have all required files in `extension/` directory
- Check Chrome console for errors

**API requests failing**
- Ensure backend is running
- Check that extension has permission to access `http://localhost:8000`
- Look in Chrome DevTools console (right-click extension > Inspect popup)

**Icon not showing**
- For MVP, icons are placeholders
- See `extension/icons/README.md` for adding real icons

## Production Deployment

### Backend

**Recommended platforms:**
- Railway
- Render
- DigitalOcean App Platform
- AWS/GCP/Azure

**Environment variables to set:**
- All variables from `.env.example`
- Set `ENVIRONMENT=production`
- Use PostgreSQL instead of SQLite
- Set up Pinecone or ChromaDB for vector storage

### Frontend

**Recommended platforms:**
- Vercel (recommended for Next.js)
- Netlify
- Railway

**Environment variables:**
- `NEXT_PUBLIC_API_URL` pointing to production backend

### Chrome Extension

**For Chrome Web Store:**
1. Create developer account ($5 one-time fee)
2. Update `manifest.json` with production API URLs
3. Create proper icons (see `extension/icons/README.md`)
4. Package extension as ZIP
5. Submit to Chrome Web Store

## Development Tips

### Hot Reload

All components support hot reload:
- **Backend**: Uses `--reload` flag with uvicorn
- **Frontend**: Next.js dev server auto-reloads
- **Extension**: Click reload icon in `chrome://extensions/`

### API Documentation

FastAPI provides auto-generated API docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Database

For development, SQLite is used by default. For production:

```python
# Use PostgreSQL
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

Run migrations:

```bash
cd backend
alembic upgrade head
```

## Next Steps

1. ✅ Complete basic setup
2. 📝 Test all three components
3. 🎨 Customize UI/branding
4. 🔐 Add authentication (Clerk recommended)
5. 💳 Integrate payments (Stripe)
6. 🚀 Deploy to production

## Getting Help

- Check the main README.md
- Review API docs at `/docs` endpoint
- Check browser console for errors
- Review backend logs

## License

MIT
