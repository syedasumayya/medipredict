# backend/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

# 1. Initialize FastAPI app
app = FastAPI(
    title="MediPredict API",
    description="AI-Powered Symptom Checker and Triage System",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Changed to allow all origins for deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the trained AI models
# We use os.path to safely find the models in the ml_core folder
if os.path.exists("ml_core"):
    model_path = "ml_core"
# Otherwise, running locally (where ml_core is one level up)
else:
    model_path = os.path.join("..", "ml_core")

encoder = joblib.load(os.path.join(model_path, "encoder.pkl"))
disease_model = joblib.load(os.path.join(model_path, "disease_model.pkl"))
triage_model = joblib.load(os.path.join(model_path, "triage_model.pkl"))

# 3. Define the Request Data Schema
# This tells FastAPI exactly what data to expect from the user.
class SymptomRequest(BaseModel):
    symptoms: str

# 4. Define the Response Data Schema
class PredictionResponse(BaseModel):
    predicted_disease: str
    triage_level: str
    disclaimer: str

# 5. Create the API Endpoint (The core logic)
@app.post("/predict", response_model=PredictionResponse)
async def predict_disease(request: SymptomRequest):
    """
    Takes patient symptoms as text and returns the predicted disease and urgency.
    """
    # Get the text from the request
    user_input = request.symptoms

    # If the user sends empty text, return a default response
    if not user_input.strip():
        return PredictionResponse(
            predicted_disease="Unknown",
            triage_level="Unknown",
            disclaimer="Please enter valid symptoms."
        )

    # Step A: Convert the user's text into AI-readable numbers using the encoder
    embedding = encoder.encode([user_input])

    # Step B: Predict the disease
    disease_prediction = disease_model.predict(embedding)[0]

    # Step C: Predict the triage (urgency)
    triage_prediction = triage_model.predict(embedding)[0]

    # Step D: Return the results
    return PredictionResponse(
        predicted_disease=disease_prediction,
        triage_level=triage_prediction,
        disclaimer="⚠️ This is an AI educational tool and not a substitute for professional medical advice."
    )

# 6. A simple GET route just to check if the server is running
@app.get("/")
def read_root():
    return {"status": "MediPredict API is running successfully! 🚀"}