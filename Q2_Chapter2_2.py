def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is upper-case or lower-case
            offset = 65 if char.isupper() else 97
            # Decrypt character by shifting it backwards
            decrypted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted_text.append(decrypted_char)
        else:
            # Non-alphabetic characters remain the same
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def find_correct_shift(ciphertext):
    possible_decryptions = {}
    # Try all possible shifts from 1 to 13
    for shift in range(1, 14):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        possible_decryptions[shift] = decrypted_text
    return possible_decryptions

# Example usage:
ciphertext = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypted_results = find_correct_shift(ciphertext)

# Display the decrypted texts for inspection
print("Decrypted results for different shift values:\n")
for shift, decrypted_text in decrypted_results.items():
    print(f"Shift {shift}:\n{decrypted_text}\n")

print("https://github.com/Rahman421-star/Assignment-2")