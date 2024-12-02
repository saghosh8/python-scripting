# Read content from a Text file

file_name = r'\path\to\file.txt'

with open(file_name, 'r') as file:
    content = file.read()