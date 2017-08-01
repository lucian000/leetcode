#
# [349] Intersection of Two Arrays
# 
# * Easy(47.09789%)
# * Testcase Example: '[]\n[]'
# * URL: https://leetcode.com/problems/intersection-of-two-arrays
# 
# Given two arrays, write a function to compute their intersection.
# 
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# 
# 
# Note:
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [i for i in set(nums1) if i in set(nums2)]        
