# Development Guide

## Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL
- Redis (optional, for caching)

## Quick Start

1. **Clone and setup:**

   ```bash
   git clone <repository>
   cd clipkit-app
   ./scripts/dev-setup.sh
   ```

2. **Configure environment:**

   - Copy `backend/env.example` to `backend/.env`
   - Copy `frontend/env.example` to `frontend/.env.local`
   - Update with your configuration

3. **Start development servers:**

   ```bash
   # Terminal 1 - Backend
   cd backend
   source venv/bin/activate
   uvicorn app.main:app --reload

   # Terminal 2 - Frontend
   cd frontend
   npm run dev
   ```

## Project Structure

```
clipkit-app/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── core/           # Core functionality (auth, config)
│   │   ├── models/         # Database models
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utilities
│   ├── alembic/            # Database migrations
│   ├── tests/              # Backend tests
│   └── requirements.txt    # Python dependencies
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app router
│   │   ├── components/    # React components
│   │   ├── lib/           # Utilities and API
│   │   └── types/         # TypeScript types
│   └── package.json       # Node.js dependencies
├── scripts/               # Development scripts
└── docs/                  # Documentation
```

## Database

### Setup

```bash
cd backend
alembic upgrade head
```

### Create Migration

```bash
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

## Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Deployment

### Using Docker

```bash
docker-compose up -d
```

### Manual Deployment

1. Set up production database
2. Configure environment variables
3. Build and deploy backend
4. Build and deploy frontend
5. Configure domain and SSL

## Code Style

### Backend (Python)

- Use Black for formatting
- Use isort for import sorting
- Follow PEP 8 guidelines

### Frontend (TypeScript)

- Use Prettier for formatting
- Use ESLint for linting
- Follow React best practices
