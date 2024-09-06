from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from routes import router as reservation_router

# Create an instance of the FastAPI application
app = FastAPI(title="Reservation Booking API", version="1.0.0")

# Allow Cross-Origin Requests from all origins (useful for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; adjust this for production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routes from the routes module
app.include_router(reservation_router, prefix="/api")

# Define models for API responses (if needed)
class ErrorResponse(BaseModel):
    detail: str

# Root endpoint
@app.get("/", response_model=str)
async def root():
    """
    Root endpoint to check if the server is running.

    Returns:
        str: A message indicating that the server is running.
    """
    return "Welcome to the Reservation Booking API!"

# Include other routes and services here
# For example, you might include additional routers for different modules

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
