# -----------------------------------------------------------
# Pattern Printing
# -----------------------------------------------------------
# Problem Description :
# Given an integer N, print an inverted isosceles triangle of stars
# such that the height of the triangle is N

# Problem Input : 7

# Problem Example :
# If input : N = 4
# Output : *******
#           *****
#            ***
#             *
# -----------------------------------------------------------


# A Python program to print an inverted isosceles triangle of stars
# such that the height of the triangle is N

N = int(input("Enter the value of the integer: "))

for i in range(N, 0, -1):         # For creating the height of the isosceles triangle
    for space in range(N - i):    # For adding the whitespace at the beginning of every line/row
        print(" ", end="")
    for row in range(2 * i - 1):  # For adding the number of '*' at each line/row of the isosceles triangle
        print('*', end='')
    print()
