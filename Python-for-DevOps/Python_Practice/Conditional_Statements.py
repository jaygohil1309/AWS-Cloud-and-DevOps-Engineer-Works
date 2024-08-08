"""

1) If_______Else.....
2) If___Elif___Else.....
3) Nested___If___Else.....

"""
# 1) IF____Else........

# age = 21

# if(age >= 18):
#     print("You are eligible for vote and licence")
# else:
#     print("Not eligible")

# 2) Else____If.......

# Light = input("Enter all the Signle lights :")

# if(Light == "Green"):
#     print("Go")
# elif(Light == "Yellow"):
#     print("Look")
# else:
#     print("Stop")

# Example :- Grade Students Based On Marks.....

marks = int(input("Enter a marks :"))

if marks >= 90:
    print("Grade - A")
elif marks > 90 and marks >= 80:
    print("Grade - B")
elif marks > 80 and marks >= 70:
    print("Grade - C")
elif marks > 70:
    print("Grade - D")
else:
    print("Failed")