#
# [557] Reverse Words in a String III
# 
# * Easy(59.82798%)
# * Testcase Example: '"Let's take LeetCode contest"'
# * URL: https://leetcode.com/problems/reverse-words-in-a-string-iii
# 
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be any extra space in the string.
# 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        for s0 in s.split(' '):
            ans.append(s0[::-1])
        return ' '.join(ans)
