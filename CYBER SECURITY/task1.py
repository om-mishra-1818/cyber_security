def caesar_cipher(text, shift, mode='encrypt'):
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Resulting message after encryption or decryption
    result = ""

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')

            # Perform the shift
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # If it's not a letter, leave it as is
            result += char

    return result

# User input for text, shift, and mode
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter the mode (encrypt/decrypt): ").lower()

# Encrypt or decrypt based on the mode
if mode in ['encrypt', 'decrypt']:
    transformed_text = caesar_cipher(text, shift, mode)
    print(f"The {mode}ed text is: {transformed_text}")
else:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")





def caesar_cipher(text, shift):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isupper():
            index = alphabet_upper.find(char)
            result += alphabet_upper[(index + shift) % 26]
        elif char.islower():
            index = alphabet_lower.find(char)
            result += alphabet_lower[(index + shift) % 26]
        else:
            result += char

    return result

# User input for text and shift
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

# Decrypt the text by shifting back
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)

