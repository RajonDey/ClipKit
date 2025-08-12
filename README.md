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

## 🚀 Quick Start

### Backend Setup

```bash
cd clipkit-app/backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd clipkit-app/frontend
npm install
npm run dev
```

### Extension Setup

1. Open Chrome Extensions
2. Enable Developer Mode
3. Load unpacked extension from `clipkit-extension/`

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

## 📝 License

Private - All rights reserved
