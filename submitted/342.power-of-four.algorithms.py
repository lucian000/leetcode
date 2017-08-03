#
# [342] Power of Four
# 
# * Easy(38.37682%)
# * Testcase Example: '16'
# * URL: https://leetcode.com/problems/power-of-four
# 
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# 
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
# 
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.
# 
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num>0:
            bs = bin(num)[2:]
        else:
            return False
        l = len(bs)
        return l%2==1 and sum(int(i) for i in bs)==1
