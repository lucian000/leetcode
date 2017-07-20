#
# [67] Add Binary
# 
# * Easy(32.11992%)
# * Testcase Example: '"0"\n"0"'
# * URL: https://leetcode.com/problems/add-binary
# 
# Given two binary strings, return their sum (also a binary string).
# 
# 
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = int(a)+int(b)
        anss = [0]+[int(i) for i in str(ans)]
        anss = anss[::-1]
        for i in range(len(anss)-1):
            if anss[i]>=2:
                anss[i]-=2
                anss[i+1]+=1
        anss = anss[::-1]
        ans = ''.join([str(i) for i in anss])
        return str(int(ans))
