# Match a single digit
# Pattern: \d
# Test string: "My number is 7"
# Matches: 7

import re
Test_string = "My number is 7"

output = re.findall(r'\d', Test_string)
print(output)

