import pandas
# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for index, row in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print([nato_dict.get(letter) for letter in input("Write a word: ").upper()])


