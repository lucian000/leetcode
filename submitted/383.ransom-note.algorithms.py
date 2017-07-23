#
# [383] Ransom Note
# 
# * Easy(47.06189%)
# * Testcase Example: '"a"\n"b"'
# * URL: https://leetcode.com/problems/ransom-note
# 
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return false. 
# 
# 
# Each letter in the magazine string can only be used once in your ransom note.
# 
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mdict = {}
        ind = 0
        n = len(magazine)
        for i in ransomNote:
            if i in mdict and mdict[i]:
                mdict[i]-=1
            else:
                while True:
                    if ind>=n:
                        return False
                    if magazine[ind]==i:
                        ind+=1
                        break
                    else:
                        if magazine[ind] in mdict:
                            mdict[magazine[ind]]+=1
                        else:
                            mdict[magazine[ind]]=1
                        ind+=1
        return True

