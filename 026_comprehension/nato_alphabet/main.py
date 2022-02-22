#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

print(data.to_dict())

phonetic_nato = {row.letter: row.code for (index, row) in data.iterrows()}

print(phonetic_nato)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

output_list = [phonetic_nato[letter] for letter in user_word]
print(output_list)

for c in user_word:
    print(phonetic_nato[c])