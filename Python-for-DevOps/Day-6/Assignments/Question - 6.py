
# Task 6: Identity and Membership Operators

"""

1. Create a list my_list containing a few  elements.
2. Use identity operators (is and is not) to check if two variables are the same object.
3. Use membership operators (in and not in) to check if an element is present in my_list.
4. Print the results.

"""

my_list = [1, 2, 3, 4, 5]

# Identity operators

a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators

element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)

