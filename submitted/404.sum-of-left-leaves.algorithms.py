#
# [404] Sum of Left Leaves
# 
# * Easy(46.90421%)
# * Testcase Example: '[3,9,20,null,null,15,7]'
# * URL: https://leetcode.com/problems/sum-of-left-leaves
# 
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        rt = self.sumOfLeftLeaves(root.right)
        if root.left is None:
            return rt
        if root.left.left is None and root.left.right is None:
            return root.left.val+rt
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
