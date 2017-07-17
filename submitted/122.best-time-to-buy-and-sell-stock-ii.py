#
# [122] Best Time to Buy and Sell Stock II
# 
# * Easy(46.76094%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# 
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i,p in enumerate(prices):
            if i>0 and p>prices[i-1]:
                profit += p - prices[i-1]
        return int(profit)
