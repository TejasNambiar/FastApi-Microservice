from fastapi import FastAPI, Request  # Import FastAPI framework and request object
from app.db.session import SessionLocal, engine, Base  # Import database connection and ORM setup
from app.api.productController import router  # Import product-related API router

# Initialize FastAPI app
app = FastAPI(title="FastAPI Microservice")

# Create all database tables at startup (if they don’t exist)
Base.metadata.create_all(bind=engine)

# Middleware to globally manage database sessions per request
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """
    Middleware to attach a database session to every incoming request.

    - Opens a new database session at the start of a request.
    - Assigns the session to `request.state.db` so it can be accessed in route handlers.
    - Ensures the session is closed after the request is processed.

    Args:
        request (Request): The incoming HTTP request object.
        call_next: A function that processes the request and returns a response.

    Returns:
        Response: The HTTP response object.
    """
    response = None
    try:
        request.state.db = SessionLocal()  # Create a new session for this request
        response = await call_next(request)  # Process the request
    finally:
        request.state.db.close()  # Close the database session after request processing
    return response

# ✅ Include product-related API routes
app.include_router(router, prefix='/products')  # Routes will be available under `/products`