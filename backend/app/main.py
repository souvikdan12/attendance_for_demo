from fastapi import FastAPI

# Import routers
from app.auth.routes import router as auth_router
from app.attendance.routes import router as attendance_router
from app.verification.routes import router as verification_router

# Create FastAPI app
app = FastAPI(
    title="BLE Smart Attendance (Demo)",
    version="1.0.0",
    description="Proxy-free smart attendance system using BLE (Demo Mode)"
)

# Include routers
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    attendance_router,
    prefix="/attendance",
    tags=["Attendance"]
)

app.include_router(
    verification_router,
    prefix="/verification",
    tags=["Verification"]
)

# Health check endpoint
@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "ok",
        "mode": "demo",
        "message": "Backend is running successfully"
    }
 