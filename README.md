🩺 MediPredict — AI-Powered Symptom Checker & Triage System
MediPredict is a production-grade, full-stack AI application designed to provide preliminary medical assessments based on natural language patient input. By leveraging advanced NLP (Natural Language Processing) and Machine Learning, the system analyzes user-described symptoms, predicts potential conditions, and recommends an appropriate triage level (e.g., Self-care, Consult Doctor, Emergency Room).

This project is built with a modern tech stack, fully containerized using Docker, and ready for cloud deployment.

✨ Core Features
Natural Language Understanding: Users can describe their symptoms in plain English (e.g., "my eyes are seeing blurry and I feel tired"). The AI understands the semantic context, not just keywords.
Disease Prediction: Classifies symptoms into likely medical conditions using a trained Machine Learning classifier.
Triage & Urgency Assignment: Automatically categorizes the severity of the condition to guide the user on the next best step.
Premium UI/UX: A clean, modern, and responsive interface built with Next.js and Tailwind CSS, featuring custom medical branding.
Production Ready: Fully dockerized for seamless deployment to any cloud platform (Render, AWS, Railway, etc.).
🛠️ Tech Stack
Frontend:

Next.js (React)
Tailwind CSS
Axios
Lucide React (Icons)
Backend:

FastAPI (Python)
Uvicorn (ASGI Server)
Pydantic (Data Validation)
AI / Machine Learning:

Sentence Transformers (all-MiniLM-L6-v2 for text embeddings)
Scikit-Learn (Logistic Regression for classification)
Joblib (Model serialization)
DevOps:

Docker & Docker Compose
🚀 How It Works
The user enters their symptoms into the Next.js web interface.
The frontend sends a POST request to the FastAPI backend.
The backend loads the trained SentenceTransformer model, converting the text into high-dimensional vector embeddings.
These embeddings are passed into the trained scikit-learn classifiers.
The backend returns the predicted disease and triage level to the frontend, displaying the results in a clean dashboard.
⚙️ Local Setup & Installation
To run this project locally using Docker, ensure you have Docker Desktop installed.

Clone the repository:
git clone https://github.com/YOUR_USERNAME/medipredict.gitcd medipredict
Start the application:
bash

docker-compose up --build
Access the app:
Frontend UI: http://localhost:3000
Backend API Docs: http://localhost:8000/docs
(Note: You will need to generate the AI models by running generate_data.py and train_model.py inside the ml_core folder if you wish to retrain the models).

⚠️ Medical Disclaimer
This application is an educational and demonstrative AI tool. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.
