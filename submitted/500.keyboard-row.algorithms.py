#
# [500] Keyboard Row
# 
# * Easy(59.98436%)
# * Testcase Example: '["Hello","Alaska","Dad","Peace"]'
# * URL: https://leetcode.com/problems/keyboard-row
# 
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# Note:
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keys = {k:1 for k in 'qwertyuiop'}
        keys.update({k:2 for k in 'asdfghjkl'})
        keys.update({k:3 for k in 'zxcvbnm'})
        ans=[]
        for wd in words:
            if len(set(keys[w.lower()] for w in wd))==1:
                ans.append(wd)
        return ans
