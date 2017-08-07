#
# [400] Nth Digit
# 
# * Easy(30.06142%)
# * Testcase Example: '3'
# * URL: https://leetcode.com/problems/nth-digit
# 
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
# 
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=9
        i=1
        while n>0:
            n-=f*i
            f*=10
            i+=1
        f/=9
        i-=1
        a,b = divmod(-n,i)
        num = f-1-a
        return int(str(num)[-b-1])
            
