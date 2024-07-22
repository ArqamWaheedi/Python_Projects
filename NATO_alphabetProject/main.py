import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
letter_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(letter_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    try:
        usr_input = input("Enter a word : ").upper()
        output_list = [letter_dict[n] for n in usr_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
# nato_list = [value for (key, value) in letter_dict.items() if key in letter_list]
    else:
        print(output_list)


generate_phonetic()
