import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nck_revision.settings')
django.setup()

from revision.models import Question

# List of questions
questions_data = [
    # BSN Questions
    {"course": "BSN", "question": "What is the normal range for adult blood pressure?", "answer": "120/80 mmHg"},
    {"course": "BSN", "question": "What is the first step in hand hygiene?", "answer": "Wet hands with clean running water"},
    {"course": "BSN", "question": "Define asepsis.", "answer": "The absence of microorganisms that cause disease"},
    {"course": "BSN", "question": "Name the three types of blood cells.", "answer": "Red blood cells, white blood cells, and platelets"},
    {"course": "BSN", "question": "What is the normal body temperature?", "answer": "36.5°C to 37.5°C"},
    {"course": "BSN", "question": "What is the Glasgow Coma Scale used for?", "answer": "Assessing level of consciousness in patients"},
    {"course": "BSN", "question": "Define infection control.", "answer": "Measures used to prevent spread of infections"},
    {"course": "BSN", "question": "What is the normal pulse rate for an adult?", "answer": "60–100 beats per minute"},
    {"course": "BSN", "question": "What is PPE?", "answer": "Personal Protective Equipment such as gloves, gowns, masks"},
    {"course": "BSN", "question": "Name a common site for intramuscular injections.", "answer": "Deltoid muscle"},
    {"course": "BSN", "question": "What is the first nursing action for a patient with shortness of breath?", "answer": "Assess airway, breathing, and oxygen saturation"},
    {"course": "BSN", "question": "What is the normal respiratory rate for adults?", "answer": "12–20 breaths per minute"},
    {"course": "BSN", "question": "Define patient advocacy.", "answer": "Acting in the best interest of the patient"},
    {"course": "BSN", "question": "Name a common symptom of hypoglycemia.", "answer": "Sweating, confusion, or shakiness"},
    {"course": "BSN", "question": "What is the standard duration for handwashing?", "answer": "At least 20 seconds"},

    # KRCHN Questions
    {"course": "KRCHN", "question": "What is the main goal of community health nursing?", "answer": "To promote health and prevent disease in the community"},
    {"course": "KRCHN", "question": "Name the three levels of prevention in public health.", "answer": "Primary, secondary, and tertiary prevention"},
    {"course": "KRCHN", "question": "What is immunization?", "answer": "Administration of vaccines to protect against disease"},
    {"course": "KRCHN", "question": "Define sanitation.", "answer": "Measures to maintain clean and hygienic conditions"},
    {"course": "KRCHN", "question": "What is the role of CHVs?", "answer": "Community Health Volunteers assist in health education and monitoring"},
    {"course": "KRCHN", "question": "What is the main cause of malaria?", "answer": "Plasmodium parasite transmitted by Anopheles mosquitoes"},
    {"course": "KRCHN", "question": "What is a health promotion activity?", "answer": "Educating mothers on breastfeeding"},
    {"course": "KRCHN", "question": "Define epidemiology.", "answer": "The study of disease patterns in populations"},
    {"course": "KRCHN", "question": "What is a growth monitoring chart?", "answer": "A chart to track children’s weight and height over time"},
    {"course": "KRCHN", "question": "What is the first action during a cholera outbreak?", "answer": "Ensure safe water and sanitation, provide rehydration therapy"},
    {"course": "KRCHN", "question": "Name a common waterborne disease.", "answer": "Typhoid or cholera"},
    {"course": "KRCHN", "question": "What is Vitamin A used for in children?", "answer": "Preventing blindness and supporting immunity"},
    {"course": "KRCHN", "question": "Define antenatal care.", "answer": "Regular check-ups for pregnant women to ensure health of mother and baby"},
    {"course": "KRCHN", "question": "Name one key indicator for maternal health.", "answer": "Maternal mortality rate"},
    {"course": "KRCHN", "question": "What is Integrated Management of Childhood Illness (IMCI)?", "answer": "A strategy to reduce childhood morbidity and mortality"},
]

# Create Questions in the database
for q in questions_data:
    Question.objects.create(
        course=q['course'],
        question_text=q['question'],   # <-- updated field name
        answer_text=q['answer']        # <-- updated field name
    )

print("✅ All 30 questions have been added successfully!")