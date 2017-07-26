#
# [447] Number of Boomerangs
# 
# * Easy(44.77775%)
# * Testcase Example: '[[0,0],[1,0],[2,0]]'
# * URL: https://leetcode.com/problems/number-of-boomerangs
# 
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans=0
        n=len(points)
        dist = [[0]*n]*n
        def distance(a,b):
            return sum((i-j)**2 for (i,j) in zip(a,b))
        for i,ni in enumerate(points):
            for j,nj in enumerate(points[:i]):
                d=distance(ni,nj)
                dist[i][j]=d
                dist[j][i]=d
        for i,l in enumerate(dist):
            for j,d0 in enumerate(l):
                if j!=i and j>0:
                    ans+=sum(1 for (k,d) in enumerate(l[:j]) if d==d0 and k!=i)
        return ans

