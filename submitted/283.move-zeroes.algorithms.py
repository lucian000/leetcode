#
# [283] Move Zeroes
# 
# * Easy(49.63956%)
# * Testcase Example: '[0,1,0,3,12]'
# * URL: https://leetcode.com/problems/move-zeroes
# 
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# 
# 
# For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# 
# 
# 
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros=0
        while True:
            try:
                nums.pop(nums.index(0))
                zeros+=1
            except:
                break
        nums.extend([0]*zeros)
