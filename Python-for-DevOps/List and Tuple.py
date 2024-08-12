# mark1 = 98
# mark2 = 95
# mark3 = 89
# mark4 = 87

# list = [mark1,mark2,mark3,mark4]

# marks = []
# for mark in list:
#     marks.append(mark)
# print(marks)

# marks = [85, 94, 76, 63, 48]

# print(marks[1:4]) # Slicing_Method
# print(marks[-3:-1])
# print(len(marks))

# new = ['Jay', 'Vishvam']
# marks.extend(new)
# print(marks)

# new = marks.count(85)
# print(new)

# result = marks.copy()
# print("Copied List :",result)


# TUPLE in Python :- Im-mutable......

# tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[0])
# print(tup[1])

# Practice Questions of List and Tuple :-

# Question 1) WAP to ask the user to enter names of their 3 favorite movies and store them in list.

# name1 = input("Enter Movie Name 1:")
# name2 = input("Enter Movie Name 2:")
# name3 = input("Enter Movie Name 3:")

# movies_name = [name1, name2, name3]
# print(movies_name)

# movies = []
# movies.append(input("Enter 1st Movie:"))
# movies.append(input("Enter 2st Movie:"))
# movies.append(input("Enter 3st Movie:"))

# print(movies)

# Question 2) WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list = [1,2,3,2,1]

result = list.copy()
print("Copied_List :",result)

result.reverse()
print("Palindrome :",result)