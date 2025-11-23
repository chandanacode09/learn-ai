# AI Content Explainer - Architecture Documentation

## System Overview

```
┌─────────────────┐
│  Chrome         │
│  Extension      │──┐
└─────────────────┘  │
                     │
┌─────────────────┐  │    ┌──────────────────┐
│  Next.js        │  │    │  FastAPI         │
│  Frontend       │──┼───▶│  Backend         │
└─────────────────┘  │    └──────────────────┘
                     │            │
                     └────────────┘
                                  │
                     ┌────────────┼────────────┐
                     │            │            │
                ┌────▼───┐  ┌────▼────┐  ┌───▼────┐
                │OpenAI/ │  │Database │  │Vector  │
                │Claude  │  │(SQLite/ │  │DB      │
                │API     │  │Postgres)│  │(Future)│
                └────────┘  └─────────┘  └────────┘
```

## Components

### 1. Backend API (FastAPI)

**Location**: `/backend`

**Responsibilities**:
- Content ingestion from multiple sources
- AI explanation generation
- User management
- Rate limiting
- Caching

**Key Modules**:

```
backend/
├── main.py              # App entry point, CORS, routes
├── core/
│   ├── config.py        # Settings management
│   └── database.py      # DB connection
├── models/
│   └── schemas.py       # Pydantic models
├── services/
│   ├── explanation_engine.py    # Core AI logic
│   └── content_ingestion.py     # Web scraping, PDF parsing
└── api/
    └── routes/
        ├── explanation.py       # /explain endpoints
        ├── content.py          # /content endpoints
        └── user.py             # /user endpoints
```

**API Endpoints**:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/health` | GET | Health check |
| `/api/v1/explanation/explain` | POST | Generate explanation |
| `/api/v1/explanation/followup` | POST | Answer follow-up |
| `/api/v1/explanation/example` | GET | Get demo explanation |
| `/api/v1/content/ingest/url` | POST | Ingest URL |
| `/api/v1/content/ingest/github` | POST | Ingest GitHub repo |
| `/api/v1/user/usage` | GET | Get user usage stats |

### 2. Frontend Web App (Next.js)

**Location**: `/frontend`

**Responsibilities**:
- User interface
- Explanation visualization
- User authentication (future)
- Dashboard and history (future)

**Key Components**:

```
frontend/
├── app/
│   ├── layout.tsx       # Root layout
│   ├── page.tsx         # Home page
│   └── globals.css      # Global styles
├── components/
│   ├── Header.tsx       # Navigation
│   ├── ExplainForm.tsx  # Input form
│   └── ExplanationView.tsx  # Result display
└── lib/
    ├── api.ts          # API client
    ├── types.ts        # TypeScript types
    └── utils.ts        # Utilities
```

**Pages**:

| Route | Purpose |
|-------|---------|
| `/` | Main explanation interface |
| `/dashboard` | User dashboard (future) |
| `/history` | Explanation history (future) |

### 3. Chrome Extension

**Location**: `/extension`

**Responsibilities**:
- One-click explanations
- Current page analysis
- Quick summaries

**Key Files**:

```
extension/
├── manifest.json    # Extension config
├── popup.html       # Extension popup UI
├── popup.js         # Popup logic
├── background.js    # Background service worker
└── content.js       # Content script (runs on pages)
```

**User Flow**:
1. User clicks extension icon
2. Extension reads current page URL
3. Sends URL to backend API
4. Displays summary in popup
5. Option to view full explanation in web app

## Data Flow

### Explanation Generation Flow

```
User Input (URL/Text)
    │
    ▼
Content Ingestion Service
    │
    ├─▶ Web Scraper (for URLs)
    ├─▶ GitHub API (for repos)
    └─▶ PDF Parser (for PDFs)
    │
    ▼
Clean & Preprocess Text
    │
    ▼
Explanation Engine
    │
    ├─▶ Build Prompt (based on level/mode)
    ├─▶ Call AI API (OpenAI/Anthropic)
    └─▶ Parse Response
    │
    ▼
Structured Explanation
    │
    ├─▶ Summary
    ├─▶ Detailed Explanation
    ├─▶ Key Takeaways
    ├─▶ Concepts
    ├─▶ Prerequisites
    ├─▶ Examples
    └─▶ Visual Aids
    │
    ▼
Return to Client
```

## AI Prompting Strategy

### Multi-Level Explanations

The system uses different prompts based on the selected level:

**ELI5**:
- No technical jargon
- Simple analogies
- Everyday examples

**Beginner**:
- Define technical terms
- Use relatable analogies
- Step-by-step breakdown

**Intermediate**:
- Assume basic domain knowledge
- Focus on how and why
- Include best practices

**Advanced**:
- Technical details
- Implementation considerations
- Performance implications

**Expert**:
- Deep technical analysis
- Edge cases
- Architectural decisions

### Mode-Specific Formatting

**Personal Mode**:
- Conversational tone
- "What's the buzz about"
- Quick takeaways

**Educational Mode**:
- Comprehensive learning material
- Prerequisites chain
- Study questions
- Progressive disclosure

**Professional Mode**:
- Actionable insights
- Implementation effort
- Cost analysis
- Production considerations

## Scalability Considerations

### Current (MVP) Architecture

- **Database**: SQLite (development only)
- **Caching**: In-memory (single instance)
- **AI**: Direct API calls
- **Rate Limiting**: In-memory counter

### Future Enhancements

1. **Database**:
   - PostgreSQL for production
   - User accounts and history
   - Explanation caching

2. **Vector Database**:
   - Pinecone or ChromaDB
   - RAG for improved accuracy
   - Semantic search

3. **Caching**:
   - Redis for distributed caching
   - Cache common explanations
   - Reduce API costs

4. **Queue System**:
   - Celery or BullMQ
   - Handle long-running tasks
   - Batch processing

5. **Authentication**:
   - Clerk integration
   - JWT tokens
   - API keys for developers

6. **Monitoring**:
   - Sentry for error tracking
   - Analytics for usage
   - Performance monitoring

## Security

### Current Implementation

- CORS configuration
- Input validation with Pydantic
- Environment variable management
- No XSS vulnerabilities (React escapes by default)

### Production Requirements

1. **API Security**:
   - Rate limiting (per user/IP)
   - API key authentication
   - Request signing

2. **Data Security**:
   - Encrypt sensitive data
   - Secure database connections
   - HTTPS everywhere

3. **Content Security**:
   - Sanitize user inputs
   - Validate URLs before fetching
   - Timeout on external requests

## Performance

### Optimization Strategies

1. **Content Ingestion**:
   - Cache fetched content (24 hours)
   - Parallel processing where possible
   - Timeout on slow requests

2. **AI Generation**:
   - Cache common explanations
   - Stream responses for large content
   - Optimize token usage

3. **Frontend**:
   - Code splitting
   - Lazy loading components
   - Optimize bundle size

## Cost Considerations

### API Costs (per explanation)

- OpenAI GPT-4: ~$0.03-0.06
- OpenAI GPT-3.5: ~$0.002-0.004
- Anthropic Claude: ~$0.02-0.04

### Optimization Strategies

1. **Caching**: Save 70-80% on repeat requests
2. **Token Optimization**: Trim content intelligently
3. **Tiered Models**: Use GPT-3.5 for simple explanations
4. **Batch Processing**: Process multiple requests together

## Testing Strategy

### Backend Tests

```bash
# Unit tests
pytest backend/tests/

# API tests
pytest backend/tests/api/

# Integration tests
pytest backend/tests/integration/
```

### Frontend Tests

```bash
# Component tests
npm run test

# E2E tests
npm run test:e2e
```

### Extension Tests

- Manual testing in Chrome
- Test on various websites
- Verify API communication

## Deployment

### Backend

**Recommended**: Railway, Render, or DigitalOcean

```bash
# Build
docker build -t ai-explainer-backend .

# Run
docker run -p 8000:8000 --env-file .env ai-explainer-backend
```

### Frontend

**Recommended**: Vercel (optimized for Next.js)

```bash
# Build
npm run build

# Preview
npm start
```

### Extension

**Chrome Web Store**:
1. Package as ZIP
2. Create developer account
3. Submit for review
4. Publish

## Monitoring & Analytics

### Metrics to Track

1. **Usage**:
   - Explanations generated
   - Popular content types
   - Level/mode distribution

2. **Performance**:
   - API response times
   - Error rates
   - Cache hit rates

3. **Costs**:
   - AI API usage
   - Token consumption
   - Infrastructure costs

4. **User Behavior**:
   - Conversion rates
   - Feature usage
   - Retention rates

## Future Roadmap

### Phase 2 Features

- [ ] User authentication
- [ ] Explanation history
- [ ] Team workspaces
- [ ] Slack/Teams integration
- [ ] API marketplace

### Phase 3 Features

- [ ] Fine-tuned models
- [ ] Visual diagram generation
- [ ] Learning paths
- [ ] Community contributions
- [ ] Enterprise SSO

## Contributing

See main README.md for contribution guidelines.
