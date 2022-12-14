import pandas

data = pandas.read_csv("section-026/nato-alphabet/nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()