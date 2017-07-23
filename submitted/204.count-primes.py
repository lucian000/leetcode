#
# [204] Count Primes
# 
# * Easy(26.51367%)
# * Testcase Example: '0'
# * URL: https://leetcode.com/problems/count-primes
# 
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        checklist = [True]*n
        checklist[0:2] = [False,False]
        for i in range(2,int(n**0.5)+1):
            if not checklist[i]:
                continue
            checklist[i**2:n:i]=[False]* ((n-1-i**2)//i+1)
        return sum(checklist)
