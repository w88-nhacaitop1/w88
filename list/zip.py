# Python | Sort the values of first list using second list

# Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#         list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']


# Input : list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
#         list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# Output : ['g', 'k', 'r', 'e', 'e', 'g', 's', 'f', 'o']

# Approach : Using zip()
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


# Driver code
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]

print(sort_list(x, y))
