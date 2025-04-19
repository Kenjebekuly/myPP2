import os
def count_lines(file_path):
    counter = 0
    with open(file_path, 'r') as file:
        for line in file:
            counter += 1
    return counter
print("Number of lines:", count_lines(r"C:/Users/serik/Desktop/PP2/lab6/builtin-functions/file1.py"))