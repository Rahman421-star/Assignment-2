import csv
import string
from collections import Counter

# List of common English stopwords
stopwords = set([
    'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'on', 'at', 'by', 'for',
    'in', 'out', 'to', 'of', 'off', 'up', 'down', 'as', 'is', 'it', 'this', 'that', 'these',
    'those', 'i', 'you', 'he', 'she', 'we', 'they', 'them', 'his', 'her', 'their', 'my', 'your'
])

def extract_real_words(text):

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Split text into words and convert to lowercase
    words = text.lower().split()

    # Filter out stopwords and numeric words
    filtered_words = [word for word in words if word not in stopwords and not word.isdigit()]

    return filtered_words

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
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(word_counts)

def main():
    # Path to the text file (Replace with the actual path to your text file)
    TEXT_FILE = 'combined_all_texts.txt'
    OUTPUT_CSV = 'top_30_common_words.csv'

    # Read the entire text file
    try:
        with open(TEXT_FILE, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError as e:
        print(f"Error reading text file: {e}")
        raise

    # Extract real words using only built-in methods
    real_words = extract_real_words(text)

    # Get the top 30 most common words
    top_30_words = count_top_words(real_words, top_n=30)

    # Save the results to a CSV file
    save_to_csv(top_30_words, OUTPUT_CSV)

    print(f"Top 30 words have been saved to {OUTPUT_CSV}")

    print("https://github.com/Rahman421-star/Assignment-2")

if __name__ == "__main__":
    main()
