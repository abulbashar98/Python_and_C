# Python reading reading files(.txt, .json, .csv)

# file_path_absolute_txt = "c:/Users/abulb/OneDrive/Desktop/input.txt"

# try:
#     with open(file = file_path_absolute_txt, mode = "r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("File was not found")

# except PermissionError:
#     print("You do not have permission")





# Read Json file

import json

file_path_absolute_json = "c:/Users/abulb/OneDrive/Desktop/input.json"

try:
    with open(file = file_path_absolute_json, mode = "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
        print(content["age"])
        print(content["job"])

except FileNotFoundError:
    print("File was not found")

except PermissionError:
    print("You do not have permission")



# Read .csv file

import csv

file_path_absolute_csv = "C:\\Users\\abulb\OneDrive\\Desktop/input.csv" 

try:
    with open(file = file_path_absolute_csv, mode = "r") as file:
       content = csv.reader(file)

       for line in content:
        #    print(line)
        #    print(line[0])
        #    print(line[1])
             print(line[2])


except FileNotFoundError:
    print("File was not found")

except PermissionError:
    print("You do not have permission")


