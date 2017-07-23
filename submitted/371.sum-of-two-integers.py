#
# [371] Sum of Two Integers
# 
# * Easy(51.24031%)
# * Testcase Example: '1\n2'
# * URL: https://leetcode.com/problems/sum-of-two-integers
# 
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# 
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all test cases.
# 
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        def add(x,y):
            if y==0:
                return x
            if x==0:
                return y
            return add((x^y)& 0xFFFFFFFF,((x&y)<<1)&0xFFFFFFFF)
        ans =  add(a,b)
        return ans if ans<= 0x7FFFFFFF else ~(ans^0xFFFFFFFF)        
