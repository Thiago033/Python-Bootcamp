import pandas

data = pandas.read_csv("section-026/nato-alphabet/nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

result = [phonetic_alphabet[letter] for letter in word]

print(result)