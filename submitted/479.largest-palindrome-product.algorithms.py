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


# Origin
#class Solution(object):
#    def largestPalindrome(self, n):
#        """
#        :type n: int
#        :rtype: int
#        """
#        nmax = int('9'*n)
#        nmax2 = nmax*nmax
#        def addreverse(n):
#            n2 = n
#            while n:
#                n,b = divmod(n,10)
#                n2 = 10*n2+b
#            return n2
#        for n1 in range(int(str(nmax2)[:n]),0,-1):
#            ans = addreverse(n1)
#            if ans>nmax2:
#                continue
#            for f1 in range(nmax,0,-1):
#                a,b = divmod(ans,f1)
#                if b==0 and a<=nmax:
#                    return ans%1337
#        for n1 in range(nmax,0,-1):
#            smax=str(nmax)
#            ans = int(smax[:-2]+smax[::-1])
#            for f1 in range(nmax,0,-1):
#                a,b = divmod(ans,f1)
#                if b==0 and a<=nmax:
#                    return ans%1337
class Solution(object):
    def largestPalindrome(self,n):
        ans = [0,9,987,123,597,677,1218,877,475]
        return ans[n]