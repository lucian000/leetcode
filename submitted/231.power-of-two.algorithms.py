#
# [231] Power of Two
# 
# * Easy(40.04092%)
# * Testcase Example: '1'
# * URL: https://leetcode.com/problems/power-of-two
# 
# Given an integer, write a function to determine if it is a power of two.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #return n>0 and bin(n).count('1')==1
        return n>0 and n&(n-1)==0
