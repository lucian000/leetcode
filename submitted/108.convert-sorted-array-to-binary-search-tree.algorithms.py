#
# [108] Convert Sorted Array to Binary Search Tree
# 
# * Easy(41.93645%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
# 
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def trans(nums):
            if not nums:
                return None
            if len(nums)==1:
                return TreeNode(nums[0])
            middle = int((len(nums)-1)/2)
            node = TreeNode(nums[middle])
            node.left = trans(nums[:middle])
            node.right = trans(nums[(middle+1):])
            return node
        return trans(nums)
