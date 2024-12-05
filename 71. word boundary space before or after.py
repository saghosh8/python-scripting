# Match a word boundary (space before or after a word)
# Pattern: \bword\b
# Test string: "word or sword"
# Matches: ['word']

import re
Test_string= "word or sword"
output = re.findall(r'\bword\b', Test_string)
print(output)