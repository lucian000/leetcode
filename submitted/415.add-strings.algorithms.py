#
# [415] Add Strings
# 
# * Easy(41.27827%)
# * Testcase Example: '"0"\n"0"'
# * URL: https://leetcode.com/problems/add-strings
# 
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        table = {str(i):{} for i in range(10)}
        for i in range(10):
            for j in range(i,10):
                s=i+j
                s=divmod(s,10)
                table[str(i)][str(j)]=s
                if i!=j:
                    table[str(j)][str(i)]=s
        m = 0
        if len(num1)>len(num2):
            num1,num2 = num2,num1
        ans=[]
        for n1,n2 in zip(num1[::-1],num2[::-1]):
            a,b=table[n1][n2]
            if m==1 and b==9:
                ans.append('0')
            else:
                ans.append(str(b+m))
                m=a
        table1 = table['1']
        for n2 in num2[::-1][len(num1):]:
            if m:
                if n2=='9':
                    ans.append('0')
                else:
                    ans.append(str(table1[n2][1]))
                    m=0
            else:
                ans.append(n2)
        if m:
            ans.append('1')
        return ''.join(ans[::-1])
