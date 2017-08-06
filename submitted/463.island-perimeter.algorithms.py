#
# [463] Island Perimeter
# 
# * Easy(57.17238%)
# * Testcase Example: '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
# * URL: https://leetcode.com/problems/island-perimeter
# 
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
# 
# Example:
# 
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# 
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get(inds):
            ans=0
            for i,j in inds:
                if i<0 or j<0:
                    ans+=1
                else:
                    try:
                        ans+= (grid[i][j]==0)
                    except:
                        ans+=1
            return ans
        ans=0
        for i,row in enumerate(grid):
            for j,n in enumerate(row):
                if n:
                    ans+=get(((i-1,j),(i+1,j),(i,j-1),(i,j+1)))
        return ans
