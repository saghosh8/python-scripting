# Match a string starting with a capital letter
# Test string: "Hello world"
# Matches: ['H']


import re
Test_String = "Hello world"
result = re.findall("^[A-Z].*", Test_String)
print(result)