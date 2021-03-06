#
# [198] House Robber
# 
# * Easy(38.69778%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/house-robber
# 
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
# 
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        f0,f1 = 0,0
        for i in nums:
            f0,f1 = f1,max(f1,f0+i)
        return f1
