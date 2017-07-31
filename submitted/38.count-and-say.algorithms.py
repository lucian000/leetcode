#
# [38] Count and Say
# 
# * Easy(34.36333%)
# * Testcase Example: '1'
# * URL: https://leetcode.com/problems/count-and-say
# 
# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# 
# 
# Given an integer n, generate the nth term of the count-and-say sequence.
# 
# 
# 
# Note: Each term of the sequence of integers will be represented as a string.
# 
# 
# Example 1:
# 
# Input: 1
# Output: "1"
# 
# 
# 
# Example 2:
# 
# Input: 4
# Output: "1211"
# 
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def trans(num):
            ans=[]
            for i,si in enumerate(num):
                if i==0:
                    snow = si
                    nnow = 1
                elif si==num[i-1]:
                    nnow+=1
                else:
                    ans.append(str(nnow)+snow)
                    snow = si
                    nnow = 1
            ans.append(str(nnow)+snow)
            return ''.join(ans)
        n1 = '1'
        for i in range(n-1):
            n1 = trans(n1)
        return n1
            

