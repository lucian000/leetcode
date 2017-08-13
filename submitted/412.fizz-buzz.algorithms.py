#
# [412] Fizz Buzz
# 
# * Easy(58.78511%)
# * Testcase Example: '1'
# * URL: https://leetcode.com/problems/fizz-buzz
# 
# Write a program that outputs the string representation of numbers from 1 to n.
# 
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
# 
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=list(range(1,n+1))
        for i1 in (2,5,8,11):
            for i in range(i1,n,15):
                ans[i]='Fizz'
        for i2 in (4,9):
            for i in range(i2,n,15):
                ans[i]='Buzz'
        for i in range(14,n,15):
            ans[i] = 'FizzBuzz'
        for i3 in (0,1,3,6,7,10,12,13):
            for i in range(i3,n,15):
                ans[i] = str(ans[i])
        return ans
        
