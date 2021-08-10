import pandas
nato_dict = {
    row.letter: row.code
    for index, row
    in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()
}
while True:
    try:
        word = input("Write a word: ").upper()
        letters_nato = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
    else:
        print(letters_nato)
        break
