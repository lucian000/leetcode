#
# [66] Plus One
# 
# * Easy(38.42792%)
# * Testcase Example: '[0]'
# * URL: https://leetcode.com/problems/plus-one
# 
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of the list.
# 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        m=True
        for i in range(len(digits)-1,-1,-1):
            if m:
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    m=False
                    break
            else:
                break
        if m:
            return [1]+digits
        else:
            return digits
