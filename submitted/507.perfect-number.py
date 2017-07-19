#
# [507] Perfect Number
# 
# * Easy(33.6968%)
# * Testcase Example: '28'
# * URL: https://leetcode.com/problems/perfect-number
# 
# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return False
        s = 1.0
        n = 2.0
        num = float(num)
        while n**2 <= num:
            n2 = num/n
            if n2-int(n2)==0:
                s+=n+n2
            if s>num+1:
                return False
            n+=1
        if s==num:
            return True
        else:
            return False
