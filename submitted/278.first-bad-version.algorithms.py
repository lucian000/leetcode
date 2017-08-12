#
# [278] First Bad Version
# 
# * Easy(25.12501%)
# * Testcase Example: '1 version\n1 is the first bad version.'
# * URL: https://leetcode.com/problems/first-bad-version
# 
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. 
# 
# 
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# 
# 
# 
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def find2(a,b):
            if a==b:
                return a
            mid = int((a+b)/2)
            if isBadVersion(mid):
                return find2(a,mid)
            else:
                return find2(mid+1,b)
        return find2(1,n)
