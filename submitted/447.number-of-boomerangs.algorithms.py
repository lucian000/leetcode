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
        dist = [[0]*n for i in range(n)]
        for i,ni in enumerate(points):
            for j,nj in enumerate(points[:i]):
                d=sum((i-j)**2 for (i,j) in zip(ni,nj))
                dist[i][j]=d
                dist[j][i]=d
        for i,l in enumerate(dist):
            count = {}            
            for j in l:
                count[j] = count.get(j,0)+1
            for j in count:
                if count[j]>1:
                    ans+=count[j]*(count[j]-1)
        return ans

