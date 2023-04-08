# -----------------------------------------------------------
# Pattern Printing
# -----------------------------------------------------------
# Problem Description :
# Given an array A of positive integers. Your task is to find the leaders in the array. 
# An element of array is leader if it is greater than or equal to all the elements to its right side. 
# The rightmost element is always a leader.

# # Problem Input : 
# n = 6
# A[] = {16,17,4,3,5,2}

# Output: 
#   17 5 2

# Explanation:
#   The first leader is 17 as it is greater than all the elements to its right. 
#   Similarly, the next leader is 5. The right most element is always a leader so it is also included.

# -----------------------------------------------------------

# A Python program
def find_leaders(arr):
    n = len(arr)
    leaders = [arr[-1]] # initialize with the rightmost element
    max_so_far = arr[-1] # initialize the maximum value seen so far

    # iterate the array from right to left
    for i in range(n-2, -1, -1):
        if arr[i] >= max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]

    leaders.reverse() # reverse the list to get the leaders in the original order
    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr)) # Output: [17, 5, 2]
        
