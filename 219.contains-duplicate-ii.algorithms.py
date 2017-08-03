#
# [219] Contains Duplicate II
# 
# * Easy(32.23876%)
# * Testcase Example: '[]\n0'
# * URL: https://leetcode.com/problems/contains-duplicate-ii
# 
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
# 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k=max(len(nums)-1,k)
        for i in range(len(nums)-k):
            for j in range(i+1,i+k+1):
                if nums[i]==nums[j]:
                    return True
        return False
