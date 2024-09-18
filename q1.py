import spacy
from collections import Counter
import csv

# Load the small English model in SpaCy
try:
    nlp = spacy.load("en_core_sci_sm")
    nlp.max_length = 2000000  # Increase max length if needed
except OSError as e:
    print(f"Error loading spaCy model: {e}")
    raise
except Exception as e:
    print(f"Unexpected error: {e}")
    raise

def extract_real_words(text):
    """
    Function to extract real English words using SpaCy and filter out stopwords,
    punctuation, non-alphabetic tokens, and lemmatize the words.
    """
    try:
        doc = nlp(text)
    except Exception as e:
        print(f"Error processing text with spaCy: {e}")
        raise

    words = [
        token.lemma_.lower() for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return words

def process_text_in_chunks(text, chunk_size=2000000):
    """
    Function to process the text in chunks to avoid memory issues.
    """
    words = []
    for start in range(0, len(text), chunk_size):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        words.extend(extract_real_words(chunk))
    return words

def count_top_words(words, top_n=30):
    """
    Function to count the frequency of words and return the top N words.
    """
    word_freq = Counter(words)
    return word_freq.most_common(top_n)

def save_to_csv(word_counts, file_path):
    """
    Function to save the word counts to a CSV file.
    """
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Frequency'])
            writer.writerows(word_counts)
    except IOError as e:
        print(f"Error writing to CSV: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def main():
    # Path to the text file (Ensure the file path is correct)
    TEXT_FILE = 'combined_all_texts.txt'
    OUTPUT_CSV = 'top_30_common_words.csv'

    try:
        with open(TEXT_FILE, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError as e:
        print(f"Error reading text file: {e}")
        print(f"Ensure the file {TEXT_FILE} exists.")
        raise
    except IOError as e:
        print(f"Error reading text file: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

    # Extract real words using NLP in chunks
    real_words = process_text_in_chunks(text)

    # Get the top 30 most common words
    top_30_words = count_top_words(real_words, top_n=30)

    # Save the results to a CSV file
    save_to_csv(top_30_words, OUTPUT_CSV)

    print(f"Top 30 words have been saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
