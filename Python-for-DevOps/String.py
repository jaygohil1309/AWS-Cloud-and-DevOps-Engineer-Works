
# # 1) Concatenation and Length :-

# a = "Hello"
# b = "World!"

# # str = a + " " + b # Concatenation
# str = a + b
# print(str)
# print(len(str)) # Length

# ' Single Quote '
# " Double Quote "
# """ Triple Quote """

# str1 = "My name is Jay Gohil.\nI am from kodinar." # Used for Create a new line.........
# str2 = "I am a AWS and DevOps Engineer.\tMy company name is The One Technologies." # Used for Create a space between two lines.

# print(str1)
# print(str2)


# 2) String_Indexing :-

# str = "Apna_College"
# str[2] = "n" # TypeError: 'str' object does not support item assignment....
# # char = str[4]
# # print(str[2])
# # print(str)

 
# # String_Slicing :-

# str = "Apna College"
# new_str = str[1:4] # pna
# new_str1 = str[:4] # Apna [0:4]
# new_str2 = str[5:] # pna [5:len(str)]

# print(str[5:len(str)]) # Important....

# print(new_str2)
# print(new_str1)
# print(new_str)

# Slicing with Negative Index :-

# str = "Apple"

# print(str[-3:-1]) # pl


# String Functions :-
# str = "I am a Coder."

# str1 = str.endswith("er.") # return True if string ends with substr.....
# print(str1)

# str2 = str.capitalize() # capitalize 1st char.....
# print(str2)

# str3 = str.upper() # Convert into Upper_Case all the string.....
# print(str3)

# str4 = str.replace("Coder", "Cloud and DevOps Engineer") # replaces all occurrences of Old with New.....
# print(str4)

# str5 = str.find("C") # returns 1st index of 1st occurrence.....
# print(str5) # If any words not included in this string then output is [-1].

# str6 = str.count("Coder") # Counts the occurrence of substr in string.....
# print(str6) 

# 1) WAP to input user's first name & print its length ??

# str = input("Enter Your name :")
# len_str = len(str)
# print(len_str)

# str = "Jay Gohil"
# print(len(str))

# 2) WAP to find the occurrence of "$" in a string ?

str = "jay@#*&^gohil$%#"
print(str.find("$"))
print(str.count("$"))