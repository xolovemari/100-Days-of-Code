import pandas

file = pandas.read_csv("day 26/nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (index, row) in file.iterrows()}

def generate_phonetic():
    user_word = input("Word: ").upper()
    try: 
        phonetic_code = [phonetic_alphabet[let] for let in user_word if let in phonetic_alphabet]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)

generate_phonetic()