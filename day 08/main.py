import string
from art import logo

alphabet = list(string.ascii_lowercase)
symbols = list(string.punctuation + string.digits + ' ')

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction_chosen, original_text, shift_amount):
    if direction_chosen == "encode":
        cipher_text = ""
        for letter in original_text:
            if letter in symbols:
                cipher_text += letter
            else:
                new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
                new_letter = alphabet[new_position]
                cipher_text += new_letter
        print(f"Here is the encoded result: {cipher_text}")
    elif direction_chosen == "decode":
        output_text = ""
        for letter in original_text:
            if letter in symbols:
                cipher_text += letter
            else:
                new_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
                new_letter = alphabet[new_position]
                output_text += new_letter
        print(f"Here is the encoded result: {output_text}")
    else:
        print("Invalid input, try again.")

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    if restart == 'no':
        print("Goodbye.")
    elif restart == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
    else:
        print("Invalid input, try again.")

caesar(direction, text, shift)