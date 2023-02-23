# Given two strings, copy one string to other using recursion.

# Input : s1 = "hello"
#         s2 = "geeksforgeeks"
# Output : s2 = "hello"

# Input :  s1 = "geeksforgeeks"
#          s2 = ""
# Output : s2 = "geeksforgeeks"

# Iterative:
# def myCopy(s1, s2):
#     for i in range(len(s1)):
#         s2[i] = s1[i]

# Recursive:
def myCopy(s1, s2, index):
    s2[index] = s1[index]

    if(index == len(s1) - 1):
        return

    myCopy(s1, s2, index)


    # Driver code
if __name__ == '__main__':
    s1 = "GEEKSFORGEEKS"
    s2 = ['']*(len(s1))
    index = 0
    myCopy(s1, s2, index)
    print(("".join(s2)))
