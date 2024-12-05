# Match a URL starting with 'http' or 'https'
# Test string: "Visit https://example.com or http://example.org"
# Matches: ['https://example.com', 'http://example.org']

import re
Test_string= "Visit https://example.com or http://example.org"
output = re.findall(r"\bhttps?://\S+\b", Test_string)
print(output)