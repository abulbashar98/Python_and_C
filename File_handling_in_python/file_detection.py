# File detection with python

import os

file_path1 = "C:/Python_and_C/File_handling_in_python/test.txt"
file_path2 = "C:/Users/abulb\OneDrive/Desktop/test.txt"

if os.path.exists(file_path1):
    print(f"File {file_path1} does exist")
    if os.path.isfile(file_path1):
        print(f"{file_path1} is a File")
    elif os.path.isdir(file_path1):
        print(f"{file_path1} is a directory")    

else:
    print(f"File {file_path1} does not exist")