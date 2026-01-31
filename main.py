import pandas

input_name = input('Enter name: ')
name_letters = [letter.upper() for letter in input_name]

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data_dict = {row.letter: row.code for (_,row) in nato_data.iterrows()}
#print(nato_data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
code_name = [nato_data_dict[letter] for letter in name_letters]
print(code_name)
