# Match any word starting with 'b'
# Test string: "bat ball bear batman"
# Matches: ['bat', 'ball', 'bear', 'batman']

import re
Test_string= "bat ball bear batman"
output = re.findall(r'\bb\w*', Test_string)
print(output)