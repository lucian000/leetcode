#
# [63] Unique Paths II
# 
# * Medium(31.58951%)
# * Testcase Example: '[[0]]'
# * URL: https://leetcode.com/problems/unique-paths-ii
# 
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
# 
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        dp[0][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[i][j]        
