from transformers import AutoTokenizer
from collections import Counter
import csv
import nltk
from nltk.corpus import stopwords

# Download stopwords from NLTK
nltk.download('stopwords')

# Get the list of stopwords in English from NLTK
stop_words = set(stopwords.words('english'))


def count_filtered_tokens_without_stopwords(file_path, tokenizer_name='bert-base-uncased', top_n=30,
    chunk_size=1000000):

    # Load the AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    token_counts = Counter()

    # Read the text file in chunks
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                # Tokenize the chunk
                tokens = tokenizer.tokenize(chunk)
                # Filter tokens
                filtered_tokens = [
                    token for token in tokens
                    if token.isalpha() and not token.startswith('##') and token.lower() not in stop_words
                ]
                # Update the token frequencies
                token_counts.update(filtered_tokens)
    except FileNotFoundError as e:
        print(f"Error reading text file: {e}")
        raise

    # Get the top N most common tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens


def save_to_csv(token_counts, file_path):
    """
    Function to save the token counts to a CSV file.
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Token', 'Frequency'])
        writer.writerows(token_counts)


def main():
    # Path to the text file (Replace with the actual path to your text file)
    TEXT_FILE = 'combined_all_texts.txt'
    OUTPUT_CSV = 'top_30_unique_tokens.csv'

    # Get the top 30 unique tokens using AutoTokenizer, excluding stopwords
    top_tokens = count_filtered_tokens_without_stopwords(TEXT_FILE, top_n=30)

    # Save the results to a CSV file
    save_to_csv(top_tokens, OUTPUT_CSV)

    print(f"Filtered Top 30 unique tokens without stopwords have been saved to {OUTPUT_CSV}")
    print("https://github.com/Rahman421-star/Assignment-2")

if __name__ == "__main__":
    main()
