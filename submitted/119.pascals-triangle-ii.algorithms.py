#
# [119] Pascal's Triangle II
# 
# * Easy(36.5858%)
# * Testcase Example: '0'
# * URL: https://leetcode.com/problems/pascals-triangle-ii
# 
# Given an index k, return the kth row of the Pascal's triangle.
# 
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# 
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        now = [1,1]
        for _ in range(rowIndex-1):
            new = [1]
            for i in range(len(now)-1):
                new.append(now[i]+now[i+1])
            new.append(1)
            now = new
        return now
