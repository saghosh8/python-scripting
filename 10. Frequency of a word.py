# Write a program to find the frequency of a word in a file.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
word_to_find = 'Python'

with open(file_path, 'r') as file:
    content = file.read()

word_count = content.lower().split().count(word_to_find.lower())

print(f"The word '{word_to_find}' appears {word_count} times in the file.")


# Here's a breakdown of `word_count = content.lower().split().count(word_to_find.lower())`:

# 1. src_pathsrc_path`content.lower()`src_pathsrc_path:  
#    Converts the entire content of the file to lowercase, ensuring the search is case-insensitive (so "Python" and "python" are treated as the same).

# 2. src_pathsrc_path`content.lower().split()`src_pathsrc_path:  
#    Splits the content into a list of words based on whitespace (spaces, tabs, newlines). Each word in the file is now an element in the list.

# 3. src_pathsrc_path`word_to_find.lower()`src_pathsrc_path:  
#    Converts the word you want to find to lowercase, ensuring the search is case-insensitive.

# 4. src_pathsrc_path`count(word_to_find.lower())`src_pathsrc_path:  
#    Counts how many times the lowercase version of `word_to_find` appears in the list of words (created from the file's content).