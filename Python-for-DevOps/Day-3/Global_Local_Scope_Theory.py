"""

*** Variable Scope and Lifetime :-

Variable_Scope :- In python, variables have different scopes, which determine where in
                  the code the variable can be accessed. There are mainly two types of
                  variable scopes......

        1) Local Scope :- Variables defined within a function have local scope and are
                          only accessible inside that function.....

        2) Global Scope :- Variables defined outside of any function have global scope
                           and can be accessed throughout the entire code.

"""

# Local Scope Example :-

def my_function():
    x = 10 # Local Variable.....
    print(x)

my_function()

# print(x) # This will raise an error since 'x' is not defined outside the function.....

# Global Scope Example :-

x=10
y=20

def glob_function():
    print(x+y) # This will access the global variable "x" and "y" with addition.....

glob_function()
print(x) # This will print 10

