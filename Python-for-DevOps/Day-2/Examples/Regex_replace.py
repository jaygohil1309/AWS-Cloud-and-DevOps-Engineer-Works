
"""

*** re_sub() :- can take optional arguments to control the number of replacements and 
                other behaviors.

                Replace occurrences of "brown" with "red" using re.sub().

                you can use the re.sub() function from the re module to perform regex-based replacement in strings. 

"""


import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)

print("Modified text :-", new_text)