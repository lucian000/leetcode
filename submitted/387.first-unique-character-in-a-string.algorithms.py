#
# [387] First Unique Character in a String
# 
# * Easy(46.4423%)
# * Testcase Example: '"leetcode"'
# * URL: https://leetcode.com/problems/first-unique-character-in-a-string
# 
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index=[s.index(l) for l in set(s) if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1 
