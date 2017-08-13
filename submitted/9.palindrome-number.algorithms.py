#
# [9] Palindrome Number
# 
# * Easy(35.17218%)
# * Testcase Example: '-2147483648'
# * URL: https://leetcode.com/problems/palindrome-number
# 
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# 
# Some hints:
# 
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# 
# There is a more generic way of solving this problem.
# 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        f = 10
        a = x
        while a>9:
            a = a//10
            f*=10
        while f>=100:
            f /= 10
            a = x//f
            x,b = divmod(x,10)
            if a!=b:
                return False
            f /= 10
            x-= a*f
        return True
