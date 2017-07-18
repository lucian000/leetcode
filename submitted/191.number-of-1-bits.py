#
# [191] Number of 1 Bits
# 
# * Easy(39.4213%)
# * Testcase Example: '           0 (00000000000000000000000000000000)'
# * URL: https://leetcode.com/problems/number-of-1-bits
# 
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# 
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        count = 0
        while True:
            if 2**i<=n:
                i+=1
            else:
                i-=1
                break
        for j in range(i,-1,-1):
            if 2**j<=n:
                n -= 2**j
                count+=1
        return count
