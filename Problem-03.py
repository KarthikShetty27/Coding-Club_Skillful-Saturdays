# -----------------------------------------------------------
# Pattern Printing
# -----------------------------------------------------------
# Problem Description :
# Given an integer N, print half pyramid of stars such that the height of the triangle is N
# and then create an inverted half pyramid of stars such that it only contains the outline.

# Problem Input : 6

# Problem Example :
# If input : N = 6
# Output : *
#          **
#          ***
#          ****
#          *****
#          ******
#               *
#              *
#             *
#            *
#           *
#          *
# -----------------------------------------------------------

# A Python program to print the pattern is

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print(" ")
    
for i in range(0, rows):
    print(" "*(rows-i-1),end='')
    print("*",end='\n')
        
