#
# [179] Largest Number
# 
# * Medium(22.44223%)
# * Testcase Example: '[1]'
# * URL: https://leetcode.com/problems/largest-number
# 
# Given a list of non negative integers, arrange them such that they form the largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead of an integer.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# 
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        maxn = max(nums)
        if maxn==0:
            return '0'
        self.n = len(str(maxn))+1
        nums = (str(i) for i in nums)
        nums = sorted([(self.fill(i),i) for i in nums],reverse = True)
        return ''.join(i[1] for i in nums)
    def fill(self,num):
        while len(num)<self.n:
            num+=num
        return num[:self.n]
