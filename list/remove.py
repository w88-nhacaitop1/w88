# Python | Remove all values from a list present in other list

test_list = [1, 3, 4, 6, 7]
remove_list = [3, 6]

print("The original list is : " + str(test_list))
print("The original list is : " + str(remove_list))

""" Method #1 : Using list comprehension
using list comprehension to perform task """

# * res = [i for i in test_list if i not in remove_list]
# * print("The list after performing remove operation is : " + str(res))


""" Method #2 : Using filter() + lambda """
res = filter(lambda i: i not in remove_list, test_list)
print("The list after performing remove operation is : " + str(res))

""" Method #3 : Using remove() """
# for i in remove_list:
#     try:
#         test_list.remove(i)
#     except ValueError:
#         pass

# print("The list after performing remove operation is : " + str(test_list))
