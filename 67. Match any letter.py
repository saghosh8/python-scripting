# Match any letter
# Pattern: [a-zA-Z]
# Test string: "Hello123"
# Matches: ['H', 'e', 'l', 'l', 'o']

import re

Test_string= "Hello123"

output = re.findall(r'[a-zA-Z]', Test_string)
print(output)