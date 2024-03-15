"""

*** re.search() :- This function scans through the entire string to find a match for the
                   pattern. It returns a match object if a match is found anywhere in the string; otherwise, it returns None.

"""

import re

text = "The quick brown fox"

# pattern = r"brown"
pattern = r"The quick brown fox"

search = re.search(pattern, text)

if search:
    print("Pattern Found :-", search.group())
else:
    print("Pattern not found")