#
# [88] Merge Sorted Array
# 
# * Easy(31.94655%)
# * Testcase Example: '[1]\n1\n[]\n0'
# * URL: https://leetcode.com/problems/merge-sorted-array
# 
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
# 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ind = 0
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            return
        for i in nums2[:n]:
            while i>nums1[ind]:
                ind+=1
            for ind2 in range(m,ind,-1):
                nums1[ind2] = nums1[ind2-1]
            nums1[ind] = i             
