#
# [14] Longest Common Prefix
# 
# * Easy(31.43669%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/longest-common-prefix
# 
# Write a function to find the longest common prefix string amongst an array of strings.
# 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        if '' in strs:
            return ''
        str1 = strs.pop(0)
        maxi = min(len(i) for i in strs)-1
        for i,ni in enumerate(str1):
            if i>maxi:
                i-=1
                break
            brk = False
            for j in strs:
                if j[i]!=ni:
                    brk=True
                    i-=1
                    break
            if brk:
                break
        return str1[:(i+1)]
                        
