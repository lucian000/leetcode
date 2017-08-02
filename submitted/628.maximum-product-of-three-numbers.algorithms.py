#
# [628] Maximum Product of Three Numbers
# 
# * Easy(45.10562%)
# * Testcase Example: '[1,2,3]'
# * URL: https://leetcode.com/problems/maximum-product-of-three-numbers
# 
# Given an integer array, find three numbers whose product is maximum and output the maximum product.
# 
# Example 1:
# 
# Input: [1,2,3]
# Output: 6
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4]
# Output: 24
# 
# 
# 
# Note:
# 
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
# 
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = [i for i in nums if i<0]
        m1=nums.pop(nums.index(max(nums)))
        m2=nums.pop(nums.index(max(nums)))
        m3=nums.pop(nums.index(max(nums)))
        if len(neg)<2:
            return m1*m2*m3
        else:
            n1 = neg.pop(neg.index(min(neg)))
            n2 = neg.pop(neg.index(min(neg)))
            return max(m1*m2*m3,m1*n1*n2)
