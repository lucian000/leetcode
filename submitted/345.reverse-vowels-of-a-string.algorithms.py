#
# [345] Reverse Vowels of a String
# 
# * Easy(38.39754%)
# * Testcase Example: '"hello"'
# * URL: https://leetcode.com/problems/reverse-vowels-of-a-string
# 
# Write a function that takes a string as input and reverse only the vowels of a string.
# 
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# 
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        isvowel = [i in 'aeiouAEIOU' for i in s]
        vowels = [i for i in s if i in "aeiouAEIOU"][::-1]
        j=0
        for i in range(len(s)):
            if isvowel[i]:
                s[i]=vowels[j]
                j+=1
        return ''.join(s)
