# ml_core/generate_data.py
import pandas as pd
import random

print("Generating a large, realistic dataset using Data Augmentation...")

# Realistic symptom templates and variations for 8 diseases
# ml_core/generate_data.py (Replace the 'diseases' variable inside this file)
diseases = {
    "Common Cold": {
        "templates": [
            "I have a {sev} fever, runny nose, and a persistent cough.",
            "My throat hurts and I keep sneezing constantly.",
            "I'm feeling congested with a mild headache and sore throat.",
            "I have a cold with a {sev} cough and watery eyes."
        ],
        "vars": {"sev": ["mild", "high", "slight", "bad"]},
        "triage": "Self-care"
    },
    "Migraine": {
        "templates": [
            "I have a {pain} headache {loc} and feel nauseous.",
            "Bright lights hurt my eyes and I feel dizzy.",
            "There is a severe throbbing pain in my head, making me want to vomit.",
            "I feel a {pain} pain {loc} that pulses."
        ],
        "vars": {"pain": ["severe", "throbbing", "splitting", "dull"], "loc": ["on one side", "behind my eyes", "at the front", "in the back"]},
        "triage": "Consult Doctor"
    },
    "Refractive Error (Eye Issue)": {
        "templates": [
            "My eyes are seeing blurry and I can't focus on distant objects.",
            "I have to squint to read signs far away, my eyesight is weak.",
            "Things look fuzzy and my eyes feel strained when I look at screens.",
            "I am experiencing blurry vision and my eyes get tired easily."
        ],
        "vars": {},
        "triage": "Schedule Eye Exam"
    },
    "COVID-19": {
        "templates": [
            "I lost my sense of smell, have a fever, and feel extremely tired.",
            "I have shortness of breath and a dry cough.",
            "My body aches and I have a high temperature with a sore throat.",
            "I feel exhausted and have a {sev} cough."
        ],
        "vars": {"sev": ["dry", "bad", "wet"]},
        "triage": "Consult Doctor"
    },
    "Gastroenteritis": {
        "templates": [
            "My stomach hurts, I have diarrhea, and I keep vomiting.",
            "I feel nauseous and have cramps in my lower abdomen.",
            "I have severe stomach cramps and feel like throwing up.",
            "I can't keep any food down and have loose motions."
        ],
        "vars": {},
        "triage": "Self-care / Hydration"
    },
    "Diabetes": {
        "templates": [
            "I am constantly thirsty, urinating a lot, and my vision gets blurry.",
            "I lost weight unexpectedly and feel fatigued with blurry vision.",
            "I feel extremely hungry all the time, very thirsty, and tired.",
            "I have a {symptom} and my cuts take a long time to heal."
        ],
        "vars": {"symptom": ["tingling feeling in my hands", "dry mouth and constant fatigue", "blurry vision and extreme thirst"]},
        "triage": "Schedule Appointment"
    },
    "Cardiac Issue": {
        "templates": [
            "I feel a crushing pain in my chest and my left arm hurts.",
            "I am sweating a lot and having trouble breathing.",
            "There is a tight pressure in my chest and I feel dizzy.",
            "I have {symptom} spreading to my jaw and back."
        ],
        "vars": {"symptom": ["sharp chest pain", "a heavy feeling in my chest", "radiating pain"]},
        "triage": "Emergency Room"
    },
    "Arthritis": {
        "templates": [
            "My knees are swollen, red, and stiff in the morning.",
            "I have severe joint pain in my fingers and wrists.",
            "My joints ache and it's hard to move them when I wake up.",
            "I have {symptom} in my hips and shoulders."
        ],
        "vars": {"symptom": ["chronic stiffness", "inflammation", "sharp joint pain"]},
        "triage": "Schedule Appointment"
    }
}

final_data = []

# Generate 200 unique rows per disease
for disease, info in diseases.items():
    for _ in range(200):
        template = random.choice(info["templates"])
        
        # Fill in the variables (like {sev} or {loc}) with random words
        for var, options in info["vars"].items():
            template = template.replace(f"{{{var}}}", random.choice(options))
        
        final_data.append({
            "symptom_text": template,
            "disease": disease,
            "triage": info["triage"]
        })

# Shuffle the data so diseases aren't grouped together
random.shuffle(final_data)

df = pd.DataFrame(final_data)
df.to_csv("medical_data.csv", index=False)
print(f"✅ Success! Dataset generated and saved as 'medical_data.csv' with {len(df)} rows.")