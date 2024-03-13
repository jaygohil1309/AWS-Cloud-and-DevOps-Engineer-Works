"""
*** What are Regular_Expressions and Why we use ??

==>> A Regular Expression is a special text string for describing a search pattern.

*** Regular Expression Operations :-

1) Find a word in a string.
2) Generate an iterator.
3) Match one of any of several letters.
4) Match series of range of characters.
5) Replace String.
6) Match a Single character.

==>> Package_Name ::- import re

"""

import re

# nameage = """Jay is 22 and Megha is 23 Yuvi is 25 and Suchit is 26"""

# ages = re.findall(r"\d{1,3}", nameage) # Find Two digit numbers....
# print(ages)

# names = re.findall(r'[A-Z][a-z]*', nameage) # Find names.....
# print(names)

# agedict = {} # Create Dictionary name with age.....

# x = 0
# for eachname in names:
#     agedict[eachname]=ages[x]
#     x+=1
# print(agedict)

str = "We need to inform him with the latest information"

for i in re.finditer('inform', str):
    tuple = i.span()
    print(tuple)


