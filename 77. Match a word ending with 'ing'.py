# Match a word ending with 'ing'
# Test string: "I am eating, running, and jumping"
# Matches: ['eating', 'running', 'jumping']

import re
Test_string= "I am eating, running, and jumping"
output = re.findall(r'\b\w+ing\b', Test_string)
print(output)