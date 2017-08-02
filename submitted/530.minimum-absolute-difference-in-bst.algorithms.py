#
# [530] Minimum Absolute Difference in BST
# 
# * Easy(46.98344%)
# * Testcase Example: '[1,null,3,2]'
# * URL: https://leetcode.com/problems/minimum-absolute-difference-in-bst
# 
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
# 
# 
# Example:
# 
# Input:
# 
#    1
#     \
#      3
#     /
#    2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# 
# 
# 
# 
# Note:
# There are at least two nodes in this BST.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get(node):
            if not node:
                return [],1e9
            ns1,md1 = get(node.left)
            ns2,md2 = get(node.right)
            return ns1+ns2+[node.val],min([abs(i-node.val) for i in ns1+ns2]+[md1,md2])
        ns,md=get(root)
        return md
