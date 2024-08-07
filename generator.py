import csv

# Define the data
data = [
    {"Health Issue": "Cold", "Symptom": "Runny Nose", "Common Medicines": "Antihistamines, Decongestants"},
    {"Health Issue": "Cold", "Symptom": "Sore Throat", "Common Medicines": "Throat Lozenges, Pain Relievers"},
    {"Health Issue": "Cold", "Symptom": "Cough", "Common Medicines": "Cough Syrup, Expectorants"},
    {"Health Issue": "Headache", "Symptom": "Pain", "Common Medicines": "Acetaminophen, Ibuprofen, Aspirin"},
    {"Health Issue": "Allergy", "Symptom": "Sneezing", "Common Medicines": "Antihistamines, Nasal Sprays"},
    {"Health Issue": "Fever", "Symptom": "High Temperature", "Common Medicines": "Acetaminophen, Ibuprofen"},
    {"Health Issue": "Stomach Ache", "Symptom": "Pain", "Common Medicines": "Antacids, Proton Pump Inhibitors"},
    {"Health Issue": "Muscle Pain", "Symptom": "Soreness", "Common Medicines": "NSAIDs, Muscle Relaxants"},
    {"Health Issue": "Asthma", "Symptom": "Wheezing", "Common Medicines": "Inhalers, Bronchodilators"},
    {"Health Issue": "Hypertension", "Symptom": "High Blood Pressure", "Common Medicines": "Beta Blockers, ACE Inhibitors"},
]

# Define the CSV file name
csv_file = "common_medicines_for_symptoms.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Health Issue", "Symptom", "Common Medicines"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"CSV file '{csv_file}' has been created successfully.")
