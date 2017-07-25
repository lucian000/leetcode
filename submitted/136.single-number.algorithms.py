#
# [136] Single Number
# 
# * Easy(54.22394%)
# * Testcase Example: '[1]'
# * URL: https://leetcode.com/problems/single-number
# 
# Given an array of integers, every element appears twice except for one. Find that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns={}
        for i in nums:
            if i in ns:
                ns[i]=False
            else:
                ns[i]=True
        for i in ns:
            if ns[i]:
                return i

