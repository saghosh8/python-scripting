# How do you count the occurrences of a specific log level (e.g., ERROR) in a log file?

word = "ERROR"
lower_word = word.lower()
fileName = r'\path\to\file.log'

with open(fileName, 'r') as file:
    content = file.read()
    times = content.lower().split().count(lower_word)