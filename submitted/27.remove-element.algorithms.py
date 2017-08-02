#
# [27] Remove Element
# 
# * Easy(38.7875%)
# * Testcase Example: '[3,2,2,3]\n3'
# * URL: https://leetcode.com/problems/remove-element
# 
# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# 
# 
# Example:
# Given input array nums = [3,2,2,3], val = 3
# 
# 
# Your function should return length = 2, with the first two elements of nums being 2.
# 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        delta=0
        n = len(nums)
        i=0
        while True:
            if nums[i]==val:
                delta+=1
            else:
                i+=1
            if i+delta<n:
                if delta:
                    nums[i]=nums[i+delta]
            else:
                break
        return n-delta
