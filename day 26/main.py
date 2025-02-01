import pandas
file = pandas.read_csv("day 26/nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (index, row) in file.iterrows()}

user_word = input("Word: ").upper()
letters = list(user_word)
phonetic_code = {phonetic_alphabet[let] for let in letters if let in phonetic_alphabet}
print(phonetic_code)