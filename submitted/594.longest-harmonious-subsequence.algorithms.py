#
# [594] Longest Harmonious Subsequence
# 
# * Easy(40.47758%)
# * Testcase Example: '[1,3,2,2,5,2,3,7]'
# * URL: https://leetcode.com/problems/longest-harmonious-subsequence
# 
# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
# 
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
# 
# Example 1:
# 
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# 
# 
# Note:
# The length of the input array will not exceed 20,000.
# 
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct={}
        for i in nums:
            if i in ct:
                ct[i]+=1
            else:
                ct[i]=1
        ans = 0
        for i in ct:
            if i+1 in ct:
                s=ct[i]+ct[i+1]
                if s>ans:
                    ans=s
        return ans
