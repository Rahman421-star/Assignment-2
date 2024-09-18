def process_string(s):
    # Ensure the string has at least 16 characters
    if len(s) < 16:
        return "Error: The input string must have at least 16 characters."

    # Step 1: Separate numbers and letters
    number_string = ''.join([ch for ch in s if ch.isdigit()])
    letter_string = ''.join([ch for ch in s if ch.isalpha()])

    # Step 2: Extract even numbers from the number string
    even_numbers = [int(digit) for digit in number_string if int(digit) % 2 == 0]

    # Step 3: Convert even numbers to ASCII code values
    ascii_codes_numbers = [ord(str(num)) for num in even_numbers]

    # Step 4: Extract uppercase letters from the letter string
    uppercase_letters = [ch for ch in letter_string if ch.isupper()]

    # Step 5: Convert uppercase letters to ASCII code values
    ascii_codes_letters = [ord(ch) for ch in uppercase_letters]

    return {
        'number_string': number_string,
        'letter_string': letter_string,
        'even_numbers': even_numbers,
        'ascii_codes_numbers': ascii_codes_numbers,
        'uppercase_letters': uppercase_letters,
        'ascii_codes_letters': ascii_codes_letters
    }


# Example usage:
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
result = process_string(s)
print("Number String:", result['number_string'])
print("Letter String:", result['letter_string'])
print("Even Numbers:", result['even_numbers'])
print("Even Numbers ASCII Codes:", result['ascii_codes_numbers'])
print("Uppercase Letters:", result['uppercase_letters'])
print("Uppercase Letters ASCII Codes:", result['ascii_codes_letters'])

print("https://github.com/Rahman421-star/Assignment-2")