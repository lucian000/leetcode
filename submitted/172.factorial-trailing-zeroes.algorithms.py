#
# [172] Factorial Trailing Zeroes
# 
# * Easy(35.84417%)
# * Testcase Example: '0'
# * URL: https://leetcode.com/problems/factorial-trailing-zeroes
# 
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# 
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=5
        ans=0
        while i<=n:
            ans += n//i
            i *=5
        return ans
