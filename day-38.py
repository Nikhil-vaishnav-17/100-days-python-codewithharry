# Secret Code Language Program
import random
import string

# Function to encode a message
def encode_message(original_message: str) -> str:
    words = original_message.split(' ')         # Split message into words
    encoded_words = []

    for word in words:
        if len(word) < 3:
            # Reverse short words (less than 3 characters)
            encoded_words.append(word[::-1])
        else:
            # Generate 3 random alphanumeric characters for prefix and suffix
            prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))

            # Move the first letter to the end and wrap with prefix and suffix
            transformed_word = prefix + word[1:] + word[0] + suffix
            encoded_words.append(transformed_word)

    # Join all encoded words into a single string
    encoded_message = ' '.join(encoded_words)
    return encoded_message

# Function to decode a previously encoded message
def decode_message(encoded_message: str) -> str:
    words = encoded_message.split(' ')          # Split encoded message into words
    decoded_words = []

    for word in words:
        if len(word) < 3:
            # Reverse short words (unchanged during encoding)
            decoded_words.append(word[::-1])
        else:
            # Extract the original word by removing prefix/suffix and restoring the first letter
            core_word = word[3:-3]               # Remove prefix and suffix
            original_word = core_word[-1] + core_word[:-1]  # Move last character to the front
            decoded_words.append(original_word)

    # Join all decoded words into a single string
    decoded_message = ' '.join(decoded_words)
    return decoded_message

# -------------------------------------------------------------------------------------------------------
# Main Program Execution

user_choice = None
while True:
    try:
        user_choice = int(input('Enter 1 to ENCODE a message or 0 to DECODE a message: '))
        if user_choice in (0, 1):
            break
        else:
            print("Please enter 1 or 0 only.")
    except ValueError:
        print("Invalid input. Please enter a number (1 or 0).")

# Handle user choice
if user_choice == 1:
    plain_text = input('Enter the message to encode: ')
    print("\nEncoded Message:")
    print(encode_message(plain_text))

elif user_choice == 0:
    coded_text = input('Enter the encoded message: ')
    print("\nDecoded Message:")
    print(decode_message(coded_text))
