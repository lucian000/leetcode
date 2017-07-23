#
# [438] Find All Anagrams in a String
# 
# * Easy(33.60556%)
# * Testcase Example: '"cbaebabacd"\n"abc"'
# * URL: https://leetcode.com/problems/find-all-anagrams-in-a-string
# 
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        setp = set(p)
        def count(s):
            c = {}
            for i in s:
                if i in c:
                    c[i]+=1
                else:
                    c[i]=1
            return c
        ans=[]
        np = len(p)
        cp = count(p)
        s0 = s[:np]
        cnow = {}
        for i in cp:
            cnow[i]=0
        for i in s0:
            if i in cnow:
                cnow[i]+=1
        if (not (0 in cnow.values())) and cnow==cp:
            ans.append(0)
        for i in range(1,len(s)-np+1):
            if s[i-1]==s[i+np-1]:
                if len(ans)>0 and i-1==ans[-1]:
                    ans.append(i)
                continue
            else:
                if s[i-1] in cnow:
                    cnow[s[i-1]]-=1
                if s[i+np-1] in cnow:                
                    cnow[s[i+np-1]]+=1
                else:
                    continue
            if 0 in cnow.values():
                continue
            if cnow == cp:
                ans.append(i)
        return ans

