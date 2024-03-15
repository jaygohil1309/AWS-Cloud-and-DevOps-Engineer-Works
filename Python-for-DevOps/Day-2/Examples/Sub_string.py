"""

*** Sub_string() :- 

"""

text = "Python is awesome"

substring = "is"

if substring in text:
    print(substring, "==>> Found in the text")


# Example of substring extraction using slicing.........
    
my_string = "Hello, world!"

# Extracting a substring from index 7 to the end........

substring1 = my_string[7:]
print(substring1)  # Output: "world!"

# Extracting a substring from index 0 to 4 (excluding index 4).........

substring2 = my_string[:5]
print(substring2)  # Output: "Hello"

# Extracting a substring from index 7 to 11 (excluding index 11)........

substring3 = my_string[7:12]
print(substring3)  # Output: "world"

# Using negative indices to count from the end of the string.........

substring4 = my_string[-6:-1]
print(substring4)  # Output: "world"

"""

==>> In Python slicing:

        1) string[start:end] extracts characters from index start to end-1.

        2) If start is omitted, it defaults to the beginning of the string.

        3) If end is omitted, it defaults to the end of the string.

        4) Negative indices can be used to count from the end of the string.

"""
