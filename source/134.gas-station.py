#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station
#
# Medium (29.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[4]\n[5]'
#
# 
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
# 
# 
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
# 
# 
# 
# Return the starting gas station's index if you can travel around the circuit
# once, otherwise return -1.
# 
# 
# 
# Note:
# The solution is guaranteed to be unique.
# 
#
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
