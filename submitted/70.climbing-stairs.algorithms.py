#
# [70] Climbing Stairs
# 
# * Easy(39.81319%)
# * Testcase Example: '1'
# * URL: https://leetcode.com/problems/climbing-stairs
# 
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        a,b = 1,2
        for _ in range(n-2):
            a,b = b,a+b
        return b
