import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# Import the FastAPI app to ensure it's initialized when the package is imported
from .main import app

# Initialize or configure other parts of the app if needed
logging.info("Python backend package initialized successfully.")
