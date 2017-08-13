#
# [263] Ugly Number
# 
# * Easy(39.10624%)
# * Testcase Example: '-2147483648'
# * URL: https://leetcode.com/problems/ugly-number
# 
# Write a program to check whether a given number is an ugly number.
# 
# 
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# 
# 
# 
# Note that 1 is typically treated as an ugly number.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        for i in [2,3,5]:
            while True:
                a,b = divmod(num,i)
                if b>0:
                    break
                else:
                    num=a
        return num==1
            
            
