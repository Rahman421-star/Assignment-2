import pandas as pd

def extract_text_from_csv(file_path, chunk_size=None, column_name='TEXT'):
    texts = []
    if chunk_size:
        # Process large CSV in chunks
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            if column_name in chunk.columns:
                texts.extend(chunk[column_name].dropna().tolist())
    else:
        # Process smaller CSV files at once
        df = pd.read_csv(file_path)
        if column_name in df.columns:
            texts.extend(df[column_name].dropna().tolist())
    return texts

def save_texts_to_file(texts, output_path):
    combined_text = '\n'.join(texts)
    with open(output_path, 'w') as f:
        f.write(combined_text)

# Paths to your CSV files
csv1_path = '/Users/amir/PycharmProjects/Assignment2/CSV1.csv'
csv2_path = '/Users/amir/PycharmProjects/Assignment2/CSV2.csv'
csv3_path = '/Users/amir/PycharmProjects/Assignment2/CSV3.csv'  # Large file
csv4_path = '/Users/amir/PycharmProjects/Assignment2/CSV4.csv'

# Extract text from smaller CSV files using the correct column name
texts_csv1 = extract_text_from_csv(csv1_path, column_name='TEXT')
texts_csv2 = extract_text_from_csv(csv2_path, column_name='TEXT')
texts_csv4 = extract_text_from_csv(csv4_path, column_name='TEXT')

# Extract text from large CSV3 file in chunks
chunk_size = 100000  # Adjust this if necessary
texts_csv3 = extract_text_from_csv(csv3_path, chunk_size=chunk_size, column_name='TEXT')

# Combine all texts from all CSVs
all_texts = texts_csv1 + texts_csv2 + texts_csv4 + texts_csv3

# Save the combined text to a .txt file
output_path = 'combined_all_texts.txt'
save_texts_to_file(all_texts, output_path)

print(f'Text extraction complete! Combined text saved at: {output_path}')
print("https://github.com/Rahman421-star/Assignment-2")