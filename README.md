# AI Content Explainer 🧠

An AI-powered tool that reads technical/scientific content and generates easy-to-understand insights with multiple explanation levels.

Transform any technical article, GitHub repository, or documentation into personalized explanations - from "Explain Like I'm 5" to expert-level analysis.

## ✨ Key Features

### 🎯 Multi-Level Explanations
- **ELI5**: Simple analogies anyone can understand
- **Beginner**: Gentle introduction with defined terms
- **Intermediate**: Balanced technical detail
- **Advanced**: Deep implementation insights
- **Expert**: Comprehensive architectural analysis

### 📚 Multiple Input Sources
- 🌐 Web articles and blog posts
- 🐙 GitHub repositories
- 📄 PDF documents (research papers)
- 💬 Direct text input
- 📝 Technical documentation

### 🎨 Three Explanation Modes
- **Personal**: Quick, conversational summaries
- **Educational**: Detailed learning material with prerequisites
- **Professional**: Actionable insights with implementation guidance

### 🚀 Multiple Interfaces
- **Web App**: Full-featured dashboard
- **Chrome Extension**: One-click explanations for any page
- **API**: Integrate into your own tools

## 🎥 Quick Demo

```bash
# 1. Start backend
cd backend && uvicorn main:app --reload

# 2. Start frontend
cd frontend && npm start

# 3. Open http://localhost:4200 and click "Try Example"
```

## 📖 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
- **[SETUP.md](SETUP.md)** - Complete setup guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design and architecture

## 🏗️ Project Structure

```
learn-ai/
├── backend/              # FastAPI backend
│   ├── main.py          # App entry point
│   ├── core/            # Configuration
│   ├── models/          # Data schemas
│   ├── services/        # Business logic
│   │   ├── explanation_engine.py    # AI explanation generation
│   │   └── content_ingestion.py     # Content extraction
│   └── api/routes/      # API endpoints
│
├── frontend/            # Angular web application
│   ├── app/            # Components and services
│   ├── src/            # Source files
│   └── angular.json    # Angular configuration
│
└── extension/          # Chrome extension
    ├── manifest.json   # Extension config
    ├── popup.html      # Extension UI
    └── popup.js        # Extension logic
```

## 🚀 Quick Start

See **[QUICKSTART.md](QUICKSTART.md)** for the fastest way to get started.

### Prerequisites

- Python 3.9+
- Node.js 18+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd learn-ai
```

2. **Setup Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env and add your OpenAI API key
cp .env.example .env
# Edit .env: OPENAI_API_KEY=sk-your-key

uvicorn main:app --reload
```

3. **Setup Frontend**
```bash
cd frontend
npm install
npm start
```

4. **Install Chrome Extension**
- Open `chrome://extensions/`
- Enable "Developer mode"
- Click "Load unpacked" → select `extension/` folder

## 💡 Usage Examples

### Web App

```
1. Open http://localhost:4200
2. Paste a URL or article text
3. Select explanation level (ELI5 to Expert)
4. Choose mode (Personal, Educational, Professional)
5. Click "Explain Content"
```

### Chrome Extension

```
1. Navigate to any technical article
2. Click the 🧠 extension icon
3. Select your level and mode
4. Get instant summary and key takeaways
```

### API

```bash
curl -X POST http://localhost:8000/api/v1/explanation/explain \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/article",
    "level": "intermediate",
    "mode": "personal"
  }'
```

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| Backend API | FastAPI, Python |
| AI Models | OpenAI GPT-4, Anthropic Claude |
| Frontend | Angular 17, TypeScript, RxJS |
| Styling | TailwindCSS |
| Database | SQLite (dev), PostgreSQL (prod) |
| Vector DB | Pinecone / ChromaDB (future) |
| Extension | Chrome Extension Manifest V3 |
| Auth | Clerk (future) |
| Payments | Stripe (future) |

## 🎯 Use Cases

### 1. Personal Learning
- Understanding trending tech topics
- "What's the buzz about?" summaries
- Building learning paths
- Saving interesting explanations

### 2. Educational
- Breaking down research papers
- Generating study materials
- Creating practice problems
- Identifying knowledge gaps

### 3. Professional
- Rapid codebase onboarding
- Executive summaries for stakeholders
- Technical debt analysis
- Cross-team knowledge sharing

## 🗺️ Roadmap

### ✅ Phase 1: MVP (Current)
- [x] Multi-level explanation engine
- [x] Web app interface
- [x] Chrome extension
- [x] URL, GitHub, and text support
- [x] Three explanation modes

### 📋 Phase 2: Enhanced Features
- [ ] User authentication (Clerk)
- [ ] Explanation history
- [ ] Visual diagram generation
- [ ] Learning path recommendations
- [ ] Stripe payment integration
- [ ] Team workspaces

### 🚀 Phase 3: Advanced Capabilities
- [ ] Fine-tuned domain-specific models
- [ ] RAG with vector database
- [ ] Slack/Teams integration
- [ ] API marketplace
- [ ] Community-driven explanations
- [ ] Enterprise SSO

## 📊 API Documentation

Interactive API documentation available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/explanation/explain` | POST | Generate explanation |
| `/api/v1/explanation/example` | GET | Get demo explanation |
| `/api/v1/content/ingest/url` | POST | Analyze URL |
| `/api/v1/content/ingest/github` | POST | Analyze GitHub repo |
| `/api/v1/health` | GET | Health check |

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- OpenAI for GPT models
- Anthropic for Claude
- Angular team for the powerful framework
- FastAPI for the excellent backend framework
- TailwindCSS for beautiful styling

## 📧 Support

- 📖 Check [SETUP.md](SETUP.md) for setup issues
- 🏗️ Review [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
- 💬 Open an issue for bugs or feature requests

---

**Made with 🧠 for making complex content accessible to everyone**
