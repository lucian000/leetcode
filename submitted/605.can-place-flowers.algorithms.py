#
# [605] Can Place Flowers
# 
# * Easy(29.94613%)
# * Testcase Example: '[1,0,0,0,1]\n1'
# * URL: https://leetcode.com/problems/can-place-flowers
# 
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# 
# 
# Note:
# 
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        imax = len(flowerbed)
        if imax<n:
            return False
        flowerbed = [0]+flowerbed+[0]
        i=1
        while i<=imax:
            if sum(flowerbed[(i-1):(i+2)])>0:
                i+=1
            else:
                n-=1
                i+=2
                if n<=0:
                    return True
        return n<=0
