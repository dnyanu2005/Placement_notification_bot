from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from .config import settings
from .database import engine, Base, SessionLocal
from .seed_data import seed_database
from .services.notification_service import sync_all_notifications

# Import routers
from .routers import profile, opportunities, chat, notifications, tracker, interview, resume, admin

# Background scheduler for deadline checks
scheduler = BackgroundScheduler()

def scheduled_deadline_check():
    try:
        db = SessionLocal()
        sync_all_notifications(db)
        db.close()
    except Exception as e:
        print(f"[Scheduler] Error running background deadline check: {e}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables & seed database
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_database(db)
        sync_all_notifications(db)
    finally:
        db.close()

    # Start recurring scheduler (runs every 60 minutes)
    try:
        scheduler.add_job(scheduled_deadline_check, 'interval', minutes=60, id='deadline_checker')
        scheduler.start()
    except Exception as e:
        print(f"[Lifespan] Scheduler warning: {e}")

    yield

    # Shutdown
    if scheduler.running:
        scheduler.shutdown()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="PlacePulse AI — The Right Opportunity. At the Right Time. AI Placement Notification Assistant",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(profile.router, prefix=settings.API_PREFIX)
app.include_router(opportunities.router, prefix=settings.API_PREFIX)
app.include_router(chat.router, prefix=settings.API_PREFIX)
app.include_router(notifications.router, prefix=settings.API_PREFIX)
app.include_router(tracker.router, prefix=settings.API_PREFIX)
app.include_router(interview.router, prefix=settings.API_PREFIX)
app.include_router(resume.router, prefix=settings.API_PREFIX)
app.include_router(admin.router, prefix=settings.API_PREFIX)

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "ai_mode": "Gemini Cloud LLM" if settings.GEMINI_API_KEY else "Local Deterministic AI Engine",
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
