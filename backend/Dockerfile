# backend/Dockerfile
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# 1. Install CPU-only PyTorch FIRST
RUN pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu

# 2. Copy the requirements file and install the rest of the dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the backend code
COPY backend/app.py .

# 4. Copy the AI models from the ml_core folder
COPY ml_core ./ml_core

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]