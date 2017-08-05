#
# [479] Largest Palindrome Product
# 
# * Easy(20.15188%)
# * Testcase Example: '1'
# * URL: https://leetcode.com/problems/largest-palindrome-product
# 
# Find the largest palindrome made from the product of two n-digit numbers.
#  Since the result could be very large, you should return the largest palindrome mod 1337.
# 
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# 
# 
# 
# 
# Note:
# The range of n is [1,8].
# 
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        nmax = int('9'*n)
        for n1 in range(nmax,0,-1):
            smax=str(n1)
            ans = int(smax+smax[::-1])
            for f1 in range(nmax,0,-1):
                for f2 in range(nmax,f1-1,-1):
                    prod = f1*f2
                    if prod==ans:
                        return ans%1337
                    if prod<ans:
                        break
        for n1 in range(nmax,0,-1):
            smax=str(n1)
            ans = int(smax[:-2]+smax[::-1])
            for f1 in range(nmax,0,-1):
                for f2 in range(nmax,f1-1,-1):
                    prod = f1*f2
                    if prod==ans:
                        return ans%1337
                    if prod<ans:
                        break
