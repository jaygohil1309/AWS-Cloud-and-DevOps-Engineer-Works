import re

text = "The quick brown fox"
pattern = r"brown"

# search = re.search(pattern, text)

# if search:
#     print("Pattern found:", search.group())
# else:
#     print("Pattern not found")

matches = re.findall(pattern, text)

if matches:
    print("Pattern found:", matches)
else:
    print("Pattern not found")