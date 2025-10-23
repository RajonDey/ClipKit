from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.collect import router as collect_router
from app.routes.ideas import router as ideas_router
from app.routes.clips import router as clips_router
from app.routes.tags import router as tags_router
from app.routes.db import router as db_router
from app.routes.auth import router as auth_router
from app.routes.content import router as content_router
import os

# Check if we're in development mode
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

# Configure CORS origins from environment variable
ALLOWED_ORIGINS = os.environ.get(
    "ALLOWED_ORIGINS", 
    "http://localhost:3000,http://127.0.0.1:3000"
).split(",")

app = FastAPI(
    title="ClipKit API",
    description="Content Collection & AI Generation Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint for deployment platforms"""
    return {"status": "healthy", "service": "clipkit-api"}

app.include_router(auth_router)
app.include_router(collect_router)
app.include_router(ideas_router)
app.include_router(clips_router)
app.include_router(tags_router)
app.include_router(db_router)
app.include_router(content_router, prefix="/content", tags=["content"])
