

"""

*** re_split() :- In Python, you can split strings using regular expressions using the 
                  re.split() function from the re module. This function allows you to specify a pattern and split a string based on that pattern. 

"""

import re

text = "apple,banana,orange,mango,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split_result :-", split_result)


# import re

# text = "The quick brown fox jumps over the lazy dog"
# pattern = r"\s+"  # This pattern matches one or more whitespace characters

# # Split the text using re.split()
# result = re.split(pattern, text)

# print("Original text:", text)
# print("After splitting using regex:", result)