# -----------------------------------------------------------
# Strings and Sub Strings
# -----------------------------------------------------------
# Problem Description :
# Given an alphabetic string S. The task is to count the number of sub-strings that starts and end with "a".
# Note: The starting and the ending "a" should be different and the size of sub-string can be anything but more than 1.

# Problem Input : "abnacfcabaa"

# Problem Example :
# If input = "ababa"
# Output = 3 substrings that are "aba", "ababa", "aba"
# -----------------------------------------------------------


# A Python program to count number of substrings starting and ending with "a"
def countSubStr(S, n):
    # Initialize result
    res = 0

    # Pick a starting point
    for i in range(0, n):
        if (S[i] == 'a'):

            # Search for all possible ending point
            for j in range(i + 1, n):
                if (S[j] == 'a'):
                    res = res + 1
    return res


# Driver program to test above function
print('\u0332'.join("INPUT:"))  # \u0332 is used to underline a text
S = input("\n Enter the string: ");
n = len(S)

print('\u0332'.join("\nOUTPUT:"))
print('\n', countSubStr(S, n), "substrings that are", end=" ")
for i in range(0, n):
    if (S[i] == 'a'):
        for j in range(i + 1, n):
            if (S[j] == 'a'):
                k = S[i:j + 1]
                print(k.split(","), end=" ")