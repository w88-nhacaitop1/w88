"""  937. Reorder Data in Log Files (Easy)
https://leetcode.com/problems/reorder-data-in-log-files/

You have an array of logs. Each log is a space delimited string of words.

!For each log, the first word in each log is an alphanumeric identifier.  Then, either:
    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs. It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log. 
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties. 
The digit-logs should be put in their original order.

Return the final order of the logs.

*Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
*Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"] 

!Constraints:
!0 <= logs.length <= 100
!3 <= logs[i].length <= 100
!logs[i] is guaranteed to have an identifier, and a word after the identifier. """

# TODO: Approach 1: Use sorted() with a custom Sort         [O(AlogA) & O(A)], where A is the total content of logs
# TODO: Approach 2:

from typing import List
from collections import Counter


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def func(log):
            id_, rest = log.split(" ", 1)

            key = (0, rest, id_) if rest[0].isalpha() else (1,)
            return key

        return sorted(logs, key=func)

    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sort = count.most_common()
        result = ""

        for i in range(len(sort)):
            result += ''.join([sort[i][0]]*sort[i][1])

        return result


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let3 art can", "dig2 3 6",
            "let2 own kit dig", "let1 art zero"]
    # logs = ["g1 act", "a8 act aoo"]

    s = Solution()
    print(s.reorderLogFiles(logs))

    print(s.frequencySort("Aabbc"))

# !Syntax of sorted()
# * sorted(iterable, key=None, reverse=False)
""" iterable            - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
    reverse (Optional)  - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
    key (Optional)      - A function that serves as a key for the sort comparison. Defaults to None. """
