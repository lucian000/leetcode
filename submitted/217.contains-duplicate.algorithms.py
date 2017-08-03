#
# [217] Contains Duplicate
# 
# * Easy(45.48528%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/contains-duplicate
# 
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=set()
        for ni in nums:
            if ni in n:
                return True
            else:
                n.add(ni)
        return False
