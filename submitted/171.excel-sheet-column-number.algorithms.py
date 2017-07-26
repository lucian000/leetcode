#
# [171] Excel Sheet Column Number
# 
# * Easy(46.86742%)
# * Testcase Example: '"A"'
# * URL: https://leetcode.com/problems/excel-sheet-column-number
# 
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# 
# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
# 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum((ord(si)-64)*26**i for i,si in enumerate(s[::-1]))        
