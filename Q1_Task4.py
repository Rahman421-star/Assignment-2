import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import Counter
import pandas as pd

# Load input data from file
with open('output_entites.txt', 'r') as file:
    text = file.read()

# Define a function to split text into smaller chunks
def split_text(text, max_length):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Load the SciSpacy model
nlp_scispacy = spacy.load('en_ner_bc5cdr_md')
# Increase the max_length limit to process longer chunks if needed
nlp_scispacy.max_length = 1000000

# Load the BioBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
biobert_ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Extract entities using SciSpacy for a single chunk
def extract_entities_scispacy_chunk(chunk):
    doc = nlp_scispacy(chunk)
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'CHEMICAL']
    return diseases, drugs

# Extract entities using BioBERT for a single chunk
def extract_entities_biobert_chunk(chunk):
    ner_results = biobert_ner(chunk)
    # Print out all detected entities and their labels to understand what BioBERT is recognizing
    print(ner_results)
    # Adjust filtering based on actual labels used by the model
    diseases = [result['word'] for result in ner_results if 'disease' in result['entity_group'].lower()]
    drugs = [result['word'] for result in ner_results if 'chemical' in result['entity_group'].lower() or 'drug' in result['entity_group'].lower()]
    return diseases, drugs


# Split text into smaller chunks for SciSpacy
scispacy_chunks = split_text(text, 1000000)

# Extract entities from all chunks using SciSpacy
scispacy_diseases, scispacy_drugs = [], []
for chunk in scispacy_chunks:
    diseases, drugs = extract_entities_scispacy_chunk(chunk)
    scispacy_diseases.extend(diseases)
    scispacy_drugs.extend(drugs)

# Split text into smaller chunks for BioBERT with overlap
stride = 256
biobert_chunks = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=510, stride=stride, return_overflowing_tokens=True)

biobert_diseases, biobert_drugs = [], []

# Extract entities from all chunks using BioBERT
for chunk in biobert_chunks['input_ids']:
    chunk_text = tokenizer.decode(chunk[:500], skip_special_tokens=True)  # Ensure the chunk is within 512 tokens
    diseases, drugs = extract_entities_biobert_chunk(chunk_text)
    biobert_diseases.extend(diseases)
    biobert_drugs.extend(drugs)

# Convert to sets for comparison
scispacy_diseases_set = set(scispacy_diseases)
scispacy_drugs_set = set(scispacy_drugs)
biobert_diseases_set = set(biobert_diseases)
biobert_drugs_set = set(biobert_drugs)

# Compare results
common_diseases = scispacy_diseases_set.intersection(biobert_diseases_set)
common_drugs = scispacy_drugs_set.intersection(biobert_drugs_set)

unique_scispacy_diseases = scispacy_diseases_set - biobert_diseases_set
unique_biobert_diseases = biobert_diseases_set - scispacy_diseases_set

unique_scispacy_drugs = scispacy_drugs_set - biobert_drugs_set
unique_biobert_drugs = biobert_drugs_set - scispacy_drugs_set

# Display results
print(f"Total entities detected by SciSpacy (Diseases): {len(scispacy_diseases_set)}")
print(f"Total entities detected by BioBERT (Diseases): {len(biobert_diseases_set)}")
print(f"Common diseases entities detected by both: {len(common_diseases)}")
print(f"Unique to SciSpacy (Diseases): {len(unique_scispacy_diseases)}")
print(f"Unique to BioBERT (Diseases): {len(unique_biobert_diseases)}")

print(f"\nTotal entities detected by SciSpacy (Drugs): {len(scispacy_drugs_set)}")
print(f"Total entities detected by BioBERT (Drugs): {len(biobert_drugs_set)}")
print(f"Common drug entities detected by both: {len(common_drugs)}")
print(f"Unique to SciSpacy (Drugs): {len(unique_scispacy_drugs)}")
print(f"Unique to BioBERT (Drugs): {len(unique_biobert_drugs)}")

# Most common entities
def get_most_common_entities(entities, top_n=10):
    counter = Counter(entities)
    return counter.most_common(top_n)

print("\nMost common diseases detected by SciSpacy:")
print(get_most_common_entities(scispacy_diseases))

print("\nMost common diseases detected by BioBERT:")
print(get_most_common_entities(biobert_diseases))

print("\nMost common drugs detected by SciSpacy:")
print(get_most_common_entities(scispacy_drugs))

print("\nMost common drugs detected by BioBERT:")
print(get_most_common_entities(biobert_drugs))

df = pd.DataFrame({
    'Entity Type': ['Disease', 'Drug'],
    'Total Entities Detected (SciSpacy)': [len(scispacy_diseases_set), len(scispacy_drugs_set)],
    'Total Entities Detected (BioBERT)': [len(biobert_diseases_set), len(biobert_drugs_set)],
    'Unique to SciSpacy': [len(unique_scispacy_diseases), len(unique_scispacy_drugs)],
    'Unique to BioBERT': [len(unique_biobert_diseases), len(unique_biobert_drugs)],
    'Common Entities': [len(common_diseases), len(common_drugs)],
    'Most Common (SciSpacy)': [get_most_common_entities(scispacy_diseases), get_most_common_entities(scispacy_drugs)],
    'Most Common (BioBERT)': [get_most_common_entities(biobert_diseases), get_most_common_entities(biobert_drugs)]})

# Save to CSV file
df.to_csv('ner_comparison_results.csv', index=False)
print('Results saved to ner_comparison_results.csv')
print("https://github.com/Rahman421-star/Assignment-2")