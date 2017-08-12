#
# [118] Pascal's Triangle
# 
# * Easy(38.31477%)
# * Testcase Example: '0'
# * URL: https://leetcode.com/problems/pascals-triangle
# 
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        ans=[[1]]
        now = [1]
        for _ in range(numRows-1):
            now = [i+j for (i,j) in zip([0]+now,now+[0])]
            ans.append(now)
        return ans 
