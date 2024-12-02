# Monitor a log file for errors.

log_file = "file.log"
word= "error"

with open(log_file, 'r') as file:
    content = file.read()

word_found = content.lower().split().count(word.lower())
if word_found > 0:
    print("Word Found")