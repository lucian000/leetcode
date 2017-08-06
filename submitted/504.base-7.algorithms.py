#
# [504] Base 7
# 
# * Easy(44.55638%)
# * Testcase Example: '100'
# * URL: https://leetcode.com/problems/base-7
# 
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<0:
            head='-'
            num= - num
        else:
            head=''
        ans=0
        p=1
        while num>0:
            num,b = divmod(num,7)
            ans += b*p
            p*=10
        return head+str(ans)
