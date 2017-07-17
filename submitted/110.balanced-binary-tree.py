#
# [110] Balanced Binary Tree
# 
# * Easy(37.28841%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/balanced-binary-tree
# 
# Given a binary tree, determine if it is height-balanced.
# 
# 
# 
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def lenth(tree):
            if tree==None:
                return int(0), True
            ln, lb=lenth(tree.left)
            rn,rb = lenth(tree.right)
            if (not lb) or (not rb) or (ln-rn)**2>1:
                return int(0), False
            return max(ln,rn)+1, True
        n,b = lenth(root)
        return b
