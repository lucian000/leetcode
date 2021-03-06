#
# [374] Guess Number Higher or Lower
# 
# * Easy(35.09484%)
# * Testcase Example: '10\n6'
# * URL: https://leetcode.com/problems/guess-number-higher-or-lower
# 
# We are playing the Guess Game. The game is as follows: 
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
# 
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# 
# 
# Example:
# 
# n = 10, I pick 6.
# 
# Return 6.
# 
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        while a!=n:
            gs = int((a+n)/2)
            rst = guess(gs)
            if rst==0:
                return gs
            if rst==-1:
                n=gs-1
            else:
                a=gs+1
        return a
