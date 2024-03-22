# num1 = 10
# num2 = 5

# addition = num1 + num2
# print("Value of addition:-" +  addition) # TypeError: can only concatenate str (not "int")
#                                       # to  str

# print("Value of addition:-" + str(addition)) # This is right method to concatenate(string).

num1 = 10
num2 = 5

def addition():
    result = num1 + num2
    print(result)

def multiplication():
    result1 = num1 * num2
    print(result1)

addition() # Calling the function......
multiplication()
