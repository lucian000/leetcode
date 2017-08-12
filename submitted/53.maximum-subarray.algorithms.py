#
# [53] Maximum Subarray
# 
# * Easy(39.48807%)
# * Testcase Example: '[-2,1,-3,4,-1,2,1,-5,4]'
# * URL: https://leetcode.com/problems/maximum-subarray
# 
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = max(nums)
        if maxn<=0:
             return maxn
        s = maxs = nums[0]
        for n in nums[1:]:
            s = max(s+n,n)
            if s>maxs:
                maxs = s
        return maxs
