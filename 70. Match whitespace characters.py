# Match whitespace characters
# Pattern: \s
# Test string: "Hello World"
# Matches: [' ']

import re
Test_string= "Hello World"
output = re.findall(r'\s', Test_string)
print(output)