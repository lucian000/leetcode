#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number
#
# Medium (39.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,2,3,4]'
#
# Given an array consists of non-negative integers,  your task is to count the
# number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
# 
# Example 1:
# 
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# 
# Note:
# 
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
# 
# 
# 
#
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
