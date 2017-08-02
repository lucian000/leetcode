#
# [58] Length of Last Word
# 
# * Easy(31.7755%)
# * Testcase Example: '""'
# * URL: https://leetcode.com/problems/length-of-last-word
# 
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space characters only.
# 
# 
# For example, 
# Given s = "Hello World",
# return 5.
# 
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if s:
            return len(s[-1])
        else:
            return 0
