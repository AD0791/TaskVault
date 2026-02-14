from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.routers import tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Runs on startup: create tables + seed data."""
    create_db_and_tables()
    yield


app = FastAPI(
    title="TaskVault API",
    description="Practice CRUD API for React Native development",
    version="1.0.0",
    lifespan=lifespan,
)

# Allow all origins (for mobile dev — phone/emulator hitting localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(tasks.router)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "taskvault-api"}
