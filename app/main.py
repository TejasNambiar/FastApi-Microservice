from fastapi import FastAPI, Request
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine, Base
from app.api.productController import router  # Import routers

app = FastAPI(title="FastAPI Microservice")

# Create tables
Base.metadata.create_all(bind=engine)

# ✅ Middleware to globally manage DB sessions
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None
    try:
        request.state.db = SessionLocal()  # Create session
        response = await call_next(request)  # Process request
    finally:
        request.state.db.close()  # Close session after request
    return response

# Include Routers
app.include_router(router, prefix='/products')