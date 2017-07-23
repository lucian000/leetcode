#
# [167] Two Sum II - Input array is sorted
# 
# * Easy(47.08634%)
# * Testcase Example: '[2,3,4]\n6'
# * URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# 
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# 
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i1,i2 = 0,len(numbers)-1
        while i1<i2:
            now = numbers[i1]+numbers[i2]
            if now>target:
                i2-=1
            elif now<target:
                i1+=1
            else:
                return [i1+1,i2+1]
