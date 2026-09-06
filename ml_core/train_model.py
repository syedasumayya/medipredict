# ml_core/train_model.py
import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Load the generated data
print("Loading data...")
df = pd.read_csv("medical_data.csv")

# 2. Load the Sentence Transformer model
print("Loading Sentence Transformer (this might take a minute to download)...")
encoder = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Convert symptom text to embeddings (vectors/numbers)
print("Encoding symptoms into AI-readable numbers...")
X_embeddings = encoder.encode(df['symptom_text'].tolist())
y_disease = df['disease']
y_triage = df['triage']

# 4. Train the Disease Classifier
print("Training Disease Classifier...")
X_train, X_test, y_train, y_test = train_test_split(X_embeddings, y_disease, test_size=0.2, random_state=42)
disease_clf = LogisticRegression(max_iter=1000)
disease_clf.fit(X_train, y_train)

# Evaluate
disease_preds = disease_clf.predict(X_test)
print("\n--- Disease Classifier Report ---")
print(classification_report(y_test, disease_preds))

# 5. Train the Triage (Urgency) Classifier
print("Training Triage Classifier...")
X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(X_embeddings, y_triage, test_size=0.2, random_state=42)
triage_clf = LogisticRegression(max_iter=1000)
triage_clf.fit(X_train_t, y_train_t)

# 6. Save the models to files
print("Saving models...")
joblib.dump(encoder, 'encoder.pkl')
joblib.dump(disease_clf, 'disease_model.pkl')
joblib.dump(triage_clf, 'triage_model.pkl')

print("\n✅ Phase 1 Complete! Models trained and saved successfully.")