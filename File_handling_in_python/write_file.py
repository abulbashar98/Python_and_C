# Write python file (.txt, .json, .csv)


txt_data = "This file was written with python"
file_path_relative = "output.txt"
file_path_absolute = "C:/Users/abulb/OneDrive/Desktop/output.txt"

# If a file does not exist then "w" mode creates a file or if it does exist with the same name and different data then "w" mode overwrites the file

with open(file = file_path_absolute, mode = "w") as file:
    file.write(txt_data)
    print(f"File {file_path_absolute} was created")












# If the file already exist then "x" mode gives a FileExistsError, otherwise creates a new file. We can catch the error with try and except

# try:
#     with open(file = file_path_relative, mode = "x") as file:
    
#         file.write(txt_data)
#         print(f"File {file_path_relative} was created")
    
# except FileExistsError:
#         print(f"File {file_path_relative} already exists")



# If there is a file already then "a" mode appends the data into the existing file, otherwise "a" creates a new file with that file_name

# with open(file = file_path_relative, mode = "a") as file:
#         file.write(txt_data + "\n")
#         print(f"File {file_path_relative} was appended")




# Write a file with a list data

employees = ["sam", "jack", "ryan", "adam"]

file_path_relative_txt = "List_output.txt"

try:
    with open(file = file_path_relative_txt, mode = "x") as file:
        for employee in employees:
            file.write(employee)
            print(f"File {file_path_relative_txt} was created")
except FileExistsError:
    print(f"File {file_path_relative_txt} already exists")






# Write a Json file with python

import json

file_path_relative_json = "output.json"
file_path_absolute_json = "C:/Users/abulb/OneDrive/Desktop/input.json"

employee = {
    "name" : "spongebob",
    "age" : 30,
    "job" : "cook" 
}

try:
    with open(file = file_path_absolute_json, mode = "x") as file:
        json.dump(employee, file)
        print(f"Json file {file_path_absolute_json} was created")

except FileExistsError:
    print(f"File {file_path_absolute_json} already exists")    




# Write a .csv file with python

import csv

file_path_relative_csv = "output.csv"
file_path_absolute_csv = "C:\\Users\\abulb\OneDrive\\Desktop/input.csv"

employee = [["Name", "Age", "Job"],
             ["spongebob", 30, "cook"],
             ["squidward", 24, "unemployed"],
             ["sandy", 25, "scientist"]]

try:
    with open(file = file_path_absolute_csv, mode = "x", newline = "") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        
        print(f"CSV file {file_path_absolute_csv} was created")

except FileExistsError:
    print(f"File {file_path_absolute_csv} already exists")


