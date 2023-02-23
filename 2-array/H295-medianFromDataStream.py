# 295. Find Median from Data Stream (Hard)
# https://leetcode.com/problems/find-median-from-data-stream/

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# For example,
# [2,3,4], the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.

# Example:
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum()
# findMedian() -> 2

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """

    
    def addNum(self, num: int) -> None:
        return None

    def findMedian(self) -> float:
        return 0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param2 = obj.findMedian()
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    result = obj.findMedian()

    print(result)
    



