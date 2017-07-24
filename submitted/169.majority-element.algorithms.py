#
# [169] Majority Element
# 
# * Easy(46.40481%)
# * Testcase Example: '[1]'
# * URL: https://leetcode.com/problems/majority-element
# 
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        n = int(len(nums)/2)
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            if dic[i]>n:
                return i      
