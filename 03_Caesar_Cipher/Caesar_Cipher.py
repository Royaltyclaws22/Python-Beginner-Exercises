import string

# English alphabets used by the Caesar cipher
UPPERCASE_ALPHABET = string.ascii_uppercase
LOWERCASE_ALPHABET = string.ascii_lowercase


def shift_text(text, key):
    """
    Shifts alphabetic characters using the Caesar cipher.

    Uppercase and lowercase letters are preserved.
    Non-alphabetic characters remain unchanged.

    Args:
        text (str): The text to process.
        key (int): Number of positions to shift.

    Returns:
        str: The processed text.
    """

    result = ""

    for char in text:

        if char in UPPERCASE_ALPHABET:
            alphabet = UPPERCASE_ALPHABET

        elif char in LOWERCASE_ALPHABET:
            alphabet = LOWERCASE_ALPHABET

        else:
            # Preserve spaces, numbers, and punctuation
            result += char
            continue

        # Find the character position in the selected alphabet
        index = alphabet.index(char)

        # Wrap around the alphabet using modulo arithmetic
        new_index = (index + key) % len(alphabet)

        result += alphabet[new_index]

    return result


# Encrypts text using the Caesar cipher
def encrypt(text, key):

    return shift_text(text, key)


# Decrypts text encrypted with the Caesar cipher
def decrypt(text, key):

    return shift_text(text, -key)


# Prompts the user until a valid integer key is entered
def get_key():

    while True:
        try:
            return int(input("Enter the shift key: "))
        except ValueError:
            print("Invalid input. Please enter an integer.\n")


def main():

    while True:

        print("\n=== Caesar Cipher ===")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":

            text = input("\nEnter the plaintext: ")
            key = get_key()

            encrypted = encrypt(text, key)

            print("\nEncrypted text:", encrypted)

        elif choice == "2":

            text = input("\nEnter the ciphertext: ")
            key = get_key()

            decrypted = decrypt(text, key)

            print("\nDecrypted text:", decrypted)

        elif choice == "3":

            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
