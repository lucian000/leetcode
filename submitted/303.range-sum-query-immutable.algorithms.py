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
        self.n = nums
        if not nums:
            self.acc = None
            return
        self.acc = [nums[0]]
        self.acci = 0
    def accu(self,i):
        if i>self.acci:
            for j in range(i-self.acci):
                self.acc.append(self.acc[-1]+self.n[self.acci+j+1])
            self.acci = i
        return self.acc[i]
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.acc is None:
            return 0
        if i==0:
            return self.accu(j)
        else:
            return self.accu(j)-self.accu(i-1)
