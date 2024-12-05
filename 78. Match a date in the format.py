# Match a date in the format MM/DD/YYYY
# Test string: "Today's date is 12/05/2024"
# Matches: ['12/05/2024']

import re
Test_string= "Today's date is 12/05/2024"
output = re.findall(r'\d{2}/\d{2}/\d{4}', Test_string)
print(output)