# Match a phone number (XXX-XXX-XXXX)
# Test string: "My phone is 123-456-7890"
# Matches: ['123-456-7890']

import re
Test_string= "My phone is 123-456-7890"
output = re.findall(r'\d{3}-\d{3}-\d{4}', Test_string)
print(output)