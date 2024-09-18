import spacy
import scispacy

# Load the spaCy models
nlp_sci_sm = spacy.load('en_core_sci_sm')
nlp_ner_bc5cdr = spacy.load('en_ner_bc5cdr_md')

# Test with a sample biomedical text
text = "Aspirin is often used to reduce fever and relieve pain."

# Process the text with 'en_core_sci_sm'
doc_sci_sm = nlp_sci_sm(text)
print("en_core_sci_sm Entities:")
for ent in doc_sci_sm.ents:
    print(ent.text, ent.label_)

# Process the text with 'en_ner_bc5cdr_md'
doc_ner_bc5cdr = nlp_ner_bc5cdr(text)
print("\nen_ner_bc5cdr_md Entities:")
for ent in doc_ner_bc5cdr.ents:
    print(ent.text, ent.label_)

# Load BioBERT for biomedical NER using transformers
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load the BioBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("pabRomero/BioBERT-full-finetuned-ner-pablo")
model = AutoModelForTokenClassification.from_pretrained("pabRomero/BioBERT-full-finetuned-ner-pablo")

# Create a NER pipeline
nlp_bert = pipeline("ner", model=model, tokenizer=tokenizer)

# Test BioBERT with the same text
print("\nBioBERT NER Results:")
bert_ner_results = nlp_bert(text)
for entity in bert_ner_results:
    print(entity['word'], entity['entity'], entity['score'])

print("https://github.com/Rahman421-star/Assignment-2")