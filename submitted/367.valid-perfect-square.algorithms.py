#
# [367] Valid Perfect Square
# 
# * Easy(38.05184%)
# * Testcase Example: '16'
# * URL: https://leetcode.com/problems/valid-perfect-square
# 
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# 
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# 
# Input: 16
# Returns: True
# 
# 
# 
# Example 2:
# 
# Input: 14
# Returns: False
# 
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.
# 
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = float(num)**0.5
        if n-int(n)<1e-6:
            return True
        else:
            return False
