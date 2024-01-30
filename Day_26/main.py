
import pandas as pd
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_dict = df.set_index('letter')['code'].to_dict()

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
code_run = True

while code_run:
    name = input("Please input a word you want to obtain in phonetic NATO code: ").upper().strip()
    phonetic_code = [nato_dict[letter] for letter in name if letter in nato_dict]
    print(phonetic_code)
    response = input("Do you want to continue? Y/N ").upper().strip()
    if response == "Y":
        #Used that since the other methods of clearing the terminal did not work
        print('\n' * 100)
    elif response == "N":
        print("Thank you for using this program.")
        code_run = False
    else:
        print("Invalid input. Please enter Y or N.")

