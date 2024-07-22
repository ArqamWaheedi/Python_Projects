import json

with open("data.json", "r") as data_file:
    # Reading old data
    data = json.load(data_file)

    print(data)
