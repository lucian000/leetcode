#
# [205] Isomorphic Strings
# 
# * Easy(33.63116%)
# * Testcase Example: '"egg"\n"add"'
# * URL: https://leetcode.com/problems/isomorphic-strings
# 
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
# 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicst = {}
        dicts = {}
        for i,si in enumerate(s):
            if si in dicst and dicst[si]!=t[i]:
                return False
            elif t[i] in dicts and dicts[t[i]]!=si:
                return False
            else:
                dicst[si]=t[i]
                dicts[t[i]]=si
        return True
