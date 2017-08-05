#
# [303] Range Sum Query - Immutable
# 
# * Easy(29.14846%)
# * Testcase Example: '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
# * URL: https://leetcode.com/problems/range-sum-query-immutable
# 
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n=nums        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
