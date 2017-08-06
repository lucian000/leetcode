#
# [20] Valid Parentheses
# 
# * Easy(33.28287%)
# * Testcase Example: '"["'
# * URL: https://leetcode.com/problems/valid-parentheses
# 
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair={'(':')','[':']','{':'}'}
        exp = [None]
        for i in s:
            if i==exp[-1]:
                exp.pop()
            else:
                if i in pair: #left
                    exp.append(pair[i])
                else: #right
                    return False
        if exp==[None]:
            return True
        return False
