#
# [216] Combination Sum III
# 
# * Medium(44.69265%)
# * Testcase Example: '3\n7'
# * URL: https://leetcode.com/problems/combination-sum-iii
# 
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# 
# 
# 
#  Example 1:
# Input:  k = 3,  n = 7
# Output: 
# 
# [[1,2,4]]
# 
# 
#  Example 2:
# Input:  k = 3,  n = 9
# Output: 
# 
# [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.find(k,n,1)
    def find(self,k,n,min0):
        if k==1:
            return [] if n>9 or n<min0 else [[n]]
        max0 = int((n-(k-1)*k/2)/k)
        ans = []
        for i in range(min0,max0+1):
            ans.extend([[i]+j for j in self.find(k-1,n-i,i+1)])
        return ans
