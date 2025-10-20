student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import csv
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# with open("nato_phonetic_alphabet.csv") as file:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# alpha_dict1 = pandas.DataFrame(data)
# print(alpha_dict1)
alpha_dict2 = {row.letter:row.code for (index,row) in data.iterrows()}
print(alpha_dict2)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("type a word: ").upper()
new = user_input.replace(" ", "")
output = ""
for char in new:

    output += (f"{alpha_dict2[char]} ")

print(output)