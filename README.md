# 🩺 MediPredict — AI-Powered Symptom Checker

MediPredict is a full-stack AI application that analyzes user-described symptoms, predicts possible medical conditions, and recommends a triage level such as **Self-Care, Consult Doctor, or Emergency Room**.

## ✨ Features

* 🧠 Natural language symptom understanding
* 🩺 Disease prediction using Machine Learning
* 🚨 Automated triage/urgency classification
* 🎨 Modern responsive UI
* 🐳 Dockerized for deployment

## 🛠️ Tech Stack

**Frontend**

* Next.js
* React
* Tailwind CSS
* Axios

**Backend**

* FastAPI
* Python
* Pydantic
* Uvicorn

**AI/ML**

* Sentence Transformers
* `all-MiniLM-L6-v2`
* Scikit-Learn
* Logistic Regression
* Joblib

**DevOps**

* Docker
* Docker Compose

## 🚀 How It Works

```text
User Symptoms
      ↓
Next.js Frontend
      ↓
FastAPI Backend
      ↓
Sentence Transformer
      ↓
Text Embeddings
      ↓
Logistic Regression
      ↓
Disease + Triage Prediction
      ↓
Frontend Result
```

## ⚙️ Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/medipredict.git
cd medipredict
```

Run with Docker:

```bash
docker-compose up --build
```

Open:

```text
Frontend: http://localhost:3000
API Docs: http://localhost:8000/docs
```

## 🤖 Train Models

Inside the `ml_core` folder:

```bash
python generate_data.py
python train_model.py
```

## ⚠️ Disclaimer

MediPredict is an **educational and demonstrative AI tool** and is not a substitute for professional medical advice, diagnosis, or treatment.
