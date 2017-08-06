#
# [409] Longest Palindrome
# 
# * Easy(45.30379%)
# * Testcase Example: '"abccccdd"'
# * URL: https://leetcode.com/problems/longest-palindrome
# 
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct={}
        for i in s:
            if i in ct:
                ct[i]+=1
            else:
                ct[i]=1
        central = False
        ans = 0
        for n in ct.values():
            a,b = divmod(n,2)
            if (not central) and b>0:
                central=True
            ans+=a
        return 2*ans+central
