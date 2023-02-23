# Python | Sort list containing alphanumeric values

# Input : ['k', 5, 'e', 3, 'g', 7, 0, 't']
# Output : [0, 3, 5, 7, 'e', 'g', 'k', 't']

# Input : [1, 'c', 3, 2, 'a', 'b']
# Output : [1, 2, 3, 'a', 'b', 'c']

# Approach 1 : Using sort() method
# Method #1 : List comprehension
# def sort(lst):
#     lst = [str(i) for i in lst]
#     lst.sort()
#     lst = [int(i) if i.isdigit() else i for i in lst]
#     return lst

# Method #2 : Using key function
# def sort(lst):
#     lst.sort(key=str)
#     return lst

# Approach #2 : Using sorted()
# Method #1 : Using key function
# def sort(lst):
#     return sorted(lst, key=str)

# Method #2 : lambda

def sort(lst):
    return sorted(lst, key=lambda x: (isinstance(x, str), x))


# Driver code
lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
print(sort(lst))
