# Match email addresses
# Test string: "Contact me at test@example.com"
# Matches: ['test@example.com']

import re
Test_string= "Contact me at test@example.com"
output = re.findall(r'[a-zA-Z0-9]+@+[a-zA-Z]+\.com', Test_string)
print(output)