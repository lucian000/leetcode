#
# [506] Relative Ranks
# 
# * Easy(46.76125%)
# * Testcase Example: '[5,4,3,2,1]'
# * URL: https://leetcode.com/problems/relative-ranks
# 
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
# 
# Example 1:
# 
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two athletes, you just need to output their relative ranks according to their scores.
# 
# 
# 
# Note:
# 
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        couple = [(j,i) for (i,j) in enumerate(nums)]
        couple = sorted(couple, key=lambda x:x[0],reverse=True)
        for i,c in enumerate(couple):
            if i==0:
                out = 'Gold Medal'
            elif i==1:
                out = 'Silver Medal'
            elif i==2:
                out = 'Bronze Medal'
            else:
                out = str(i+1)
            nums[c[1]] = out
        return nums
