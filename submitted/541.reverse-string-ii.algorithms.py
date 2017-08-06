#
# [541] Reverse String II
# 
# * Easy(44.07568%)
# * Testcase Example: '"abcdefg"\n2'
# * URL: https://leetcode.com/problems/reverse-string-ii
# 
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
#  The string consists of lower English letters only.
#  Length of the given string and k will in the range [1, 10000]
# 
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s0 = [i for i in s]
        i=0
        while s0[i:(i+k)]:
            s0[i:(i+k)]=s0[(i+k-1):i:-1]+[s0[i]]
            i+=2*k
        return ''.join(s0)
