# Match a word starting with 'a'
# Pattern: \ba\w*
# Test string: "apple and banana"
# Matches: ['apple', 'and']

import re
Test_string= "apple and banana"
output = re.findall(r'\ba\w*', Test_string)
print(output)