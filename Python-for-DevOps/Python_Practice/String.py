
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
# print(str)

 
# String_Slicing :-

str = "Apna College"
new_str = str[1:4] # pna
new_str1 = str[:4] # Apna [0:4]
new_str2 = str[5:] # pna [5:len(str)]

print(str[5:len(str)]) # Important....

print(new_str2)
print(new_str1)
print(new_str)