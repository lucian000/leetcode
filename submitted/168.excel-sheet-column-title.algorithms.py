#
# [168] Excel Sheet Column Title
# 
# * Easy(25.744%)
# * Testcase Example: '1'
# * URL: https://leetcode.com/problems/excel-sheet-column-title
# 
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases.
# 
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans=[]
        while n:
            n,b = divmod(n-1,26)
            ans.append(b)
        return ''.join((chr(65+i) for i in ans[::-1]))
