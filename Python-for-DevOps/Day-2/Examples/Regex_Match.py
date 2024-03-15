
"""

*** re_match() :- This function checks for a match only at the beginning of the string. 
                  If the pattern is found at the beginning, it returns a match object; otherwise, it returns None.

"""


import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

