import sys

def add(num1, num2):
    add =  num1 + num2
    return add

def sub(num1,num2):
    sub = num1 - num2
    return sub

def multi(num1, num2):
    multi = num1 * num2
    return multi

def div(num1, num2):
    div = num1 / num2
    return div

def modulus(num1, num2):
    modulus = num1 % num2
    return modulus

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

operations = {
    "add" : add,
    "sub" : sub,
    "multi" : multi,
    "div" : div,
    "modulus" : modulus
}

if operation in operations:
    output = operations[operation](num1, num2)
    print(output)
else:
    print("Invalid Operations.....")




