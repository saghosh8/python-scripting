# Match digits at the end of the string
# Pattern: \d+$
# Test string: "Price is 100"
# Matches: ['100']

import re
Test_string = "Price is 100"
output = re.findall(r"\d\w*", Test_string)
output2 = re.findall(r"\d+$", Test_string)
print(output)
print(output2)