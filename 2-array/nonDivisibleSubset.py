# Non Divisible Subset
# https://www.hackerrank.com/domains/algorithms

# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.
# For example, the array S = [19, 10, 12, 10, 24, 25, 22] and k = 4.
# One of the arrays that can be created is S'[0] = [10, 12, 25].
# Another is S'[1] = [19, 22, 24].
# After testing all permutations, the maximum length solution array has 3 elements.


def nonDivisibleSubset(k, s):
    """
    type: int
    type: List[int]
    rtype: int
    """
    count = 0

    d = {x: [] for x in range(k)}

    for i in range(n):
        d[s[i] % k].append(arr[i])

    if len(d[0]) > 0:
        count = 1

    _set = set([(x, k-x) for x in range(1, k//2 + 1)])

    for i, j in _set:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1

    return count


if __name__ == "__main__":
    # arr, k = [1, 7, 2, 4], 3
    arr, k = [19, 10, 12, 10, 24, 25, 22], 4
    n = len(arr)

    # Example:
    test = set([(x, k - x) for x in range(1, k//2 + 1)])

    result = nonDivisibleSubset(k, arr)
    print(result)
