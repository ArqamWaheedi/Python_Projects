# TODO: Create a letter using starting_letter.txt
#  for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/ARQAM/Downloads/Mail+Merge+Project+Start/Mail Merge Project "
          "Start/Input/Names/invited_names.txt") as names_file:
    x = names_file.readlines()
with open("/Users/ARQAM/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/"
          "Letters/starting_letter.txt") as file:
    t = file.read()
    # txt = x[0]
for n in x:
    stripped_name = n.strip()
    y = t.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_file:
        new_file.write(y)

