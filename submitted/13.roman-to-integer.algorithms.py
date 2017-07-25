#
# [13] Roman to Integer
# 
# * Easy(45.47838%)
# * Testcase Example: '"DCXXI"'
# * URL: https://leetcode.com/problems/roman-to-integer
# 
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
# 
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tb = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        if len(s)==1:
            return tb[s[0]]   
        ns = [tb[i] for i in s]
        ns2 = ns[1:]
        ans=0
        for i in range(len(ns2)):
            if ns[i]<ns2[i]:
                ans-=ns[i]
            else:
                ans+=ns[i]
        return ans+ns[-1]
