#
# [258] Add Digits
# 
# * Easy(51.03986%)
# * Testcase Example: '0'
# * URL: https://leetcode.com/problems/add-digits
# 
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 
# 
# 
# 
# For example:
# 
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num:
            return (num-1)%9+1
        else:
            return 0        
