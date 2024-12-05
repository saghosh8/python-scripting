# Match words with 3 letters
# Test string: "The cat and dog"
# Matches: ['The', 'cat', 'and', 'dog']

import re
Test_string= "The cat and dogs"
output = re.findall(r'\b\w{3}\b', Test_string)
print(output)