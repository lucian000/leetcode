#
# [290] Word Pattern
# 
# * Easy(32.93867%)
# * Testcase Example: '"abba"\n"dog cat cat dog"'
# * URL: https://leetcode.com/problems/word-pattern
# 
# Given a pattern and a string str, find if str follows the same pattern.
#  Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# 
# Examples:
# 
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 
# 
# 
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
# 
# 
# Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases.
# 
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern)!=len(str):
            return False
        relat = {}
        for i,si in enumerate(pattern):
            if si in relat:
                if relat[si]!=str[i]:
                    return False
            else:
                if str[i] in relat.values():
                    return False
                relat[si]=str[i]
        return True
