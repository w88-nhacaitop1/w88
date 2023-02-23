""" 207. Course Schedule (Medium)
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

*Input: numCourses = 2, prerequisites = [[1,0]]
*Output: true
*Explanation: There are a total of 2 courses to take. 
*             To take course 1 you should have finished course 0. So it is possible.


*Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
*Output: false
*Explanation: There are a total of 2 courses to take. 
*             To take course 1 you should have finished course 0, and to take course 0 you should
*             also have finished course 1. So it is impossible.
 

!Constraints:
!   The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
!   You may assume that there are no duplicate edges in the input prerequisites.
!   1 <= numCourses <= 10^5
"""

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        path = [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, path):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, path):
        """
        backtracking method to check that no cycle would be formed starting from currCourse
        """
        if path[currCourse]:
            # come across a previously visited node, i.e. detect the cycle
            return True

        # before backtracking, mark the node in the path
        path[currCourse] = True

        # backtracking
        ret = False
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, path)
            if ret: break

        # after backtracking, remove the node from the path
        path[currCourse] = False
        return ret


if __name__ == "__main__":
    numCourses, prerequisites = 2, [[1, 0]]  # ? Output = true
    # numCourses, prerequisites = 2, [[1, 0], [0, 1]]  # ? Output = false

    s = Solution()
    result1 = s.canFinish(numCourses, prerequisites)

    print("[Approach 1] Result is {}".format(result1))