#
# [459] Repeated Substring Pattern
# 
# * Easy(38.10076%)
# * Testcase Example: '"abab"'
# * URL: https://leetcode.com/problems/repeated-substring-pattern
# 
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.  You may assume the given string consists of lowercase English letters only and its length  will not exceed 10000. 
# 
# Example 1:
# 
# Input: "abab"
# 
# Output: True
# 
# Explanation: It's the substring "ab" twice.
# 
# 
# 
# Example 2:
# 
# Input: "aba"
# 
# Output: False
# 
# 
# 
# Example 3:
# 
# Input: "abcabcabcabc"
# 
# Output: True
# 
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
# 
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        for i in range(2,n+1):
            a,b = divmod(n,i)
            if b==0:
                ans = True
                for j in range(n-a):
                    if s[j]!=s[j+a]:
                        ans=False
                        break
                if ans:
                    return True
        return False        
