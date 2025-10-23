# Clipkit - Content Collection & AI Generation Platform

A comprehensive SaaS platform for content creators to collect, organize, and generate content using AI.

## 🏗️ Project Structure

```
clipkit/
├── clipkit-app/           # Main application
│   ├── backend/          # FastAPI backend
│   └── frontend/         # Next.js frontend
├── clipkit-extension/    # Browser extension
└── README.md            # This file
```

## 🚀 Quick Start (Development)

### 1. Backend Setup

```bash
cd clipkit-app/backend

# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from env.example)
cp env.example .env

# IMPORTANT: Edit .env and set:
# - SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_urlsafe(32))")
# - DATABASE_URL (your PostgreSQL connection string)
# - GROQ_API_KEY (optional, for AI features)

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### 2. Frontend Setup

```bash
cd clipkit-app/frontend

# Install dependencies
npm install

# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Start development server
npm run dev
```

### 3. Extension Setup

1. Open Chrome Extensions (chrome://extensions)
2. Enable Developer Mode
3. Click "Load unpacked" and select `clipkit-extension/`

## 📋 Features

- **Content Collection**: Browser extension for collecting web content
- **AI Generation**: AI-powered content creation using multiple models
- **Subscription Tiers**: Free, Pro, and Business plans
- **User Management**: Authentication and user profiles
- **Content Organization**: Ideas, clips, and tags management

## 🔧 Development

- **Backend**: FastAPI + PostgreSQL + Alembic
- **Frontend**: Next.js + TypeScript + Tailwind CSS
- **Extension**: Vanilla JavaScript + Chrome Extension API
- **AI**: OpenAI, Anthropic, Groq integration

## 🚢 Deployment

### Backend (Railway/Render/Heroku)

1. **Set Environment Variables:**

   ```
   SECRET_KEY=<generate-random-secret>
   DATABASE_URL=<your-postgres-url>
   ALLOWED_ORIGINS=https://your-frontend-domain.com
   GROQ_API_KEY=<your-api-key> (optional)
   DEBUG=false
   ```

2. **Deploy:**
   - Point to `clipkit-app/backend` directory
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Run migrations: `alembic upgrade head`

### Frontend (Vercel/Netlify)

1. **Set Environment Variable:**

   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.com
   ```

2. **Deploy:**
   - Point to `clipkit-app/frontend` directory
   - Framework preset: Next.js
   - Build command: `npm run build`
   - Output directory: `.next`

### Health Check

Your backend includes a `/health` endpoint for monitoring:

```bash
curl https://your-backend-url.com/health
# Returns: {"status":"healthy","service":"clipkit-api"}
```

## 📝 License

Private - All rights reserved
