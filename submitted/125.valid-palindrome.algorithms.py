#
# [125] Valid Palindrome
# 
# * Easy(26.11286%)
# * Testcase Example: '""'
# * URL: https://leetcode.com/problems/valid-palindrome
# 
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# 
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# 
# 
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# 
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        import re
        s= re.sub('\W','',s).lower()
        for i in range(int(len(s)/2)):
            if s[i]!=s[-i-1]:
                return False
        return True
