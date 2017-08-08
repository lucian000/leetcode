#
# [501] Find Mode in Binary Search Tree
# 
# * Easy(38.09133%)
# * Testcase Example: '[1,null,2,2]'
# * URL: https://leetcode.com/problems/find-mode-in-binary-search-tree
# 
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
# 
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
#    1
#     \
#      2
#     /
#    2
# 
# 
# 
# return [2].
# 
# 
# Note:
# If a tree has more than one mode, you can return them in any order.
# 
# 
# Follow up:
# Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        def mode(n):
            if n.left is None and n.right is None:
                return [n.val], 1
            if n.left is None:
                mr,nr = mode(n.right)
                if nr>1:
                    return mr,nr
                else:
                    return mr+[n.val],1
            if n.right is None:
                ml,nl = mode(n.left)
                if n.val in ml:
                    return [n.val],nl+1
                elif nl>1:
                    return ml,nl
                else:
                    return ml+[n.val],1
            mr,nr = mode(n.right)
            ml,nl = mode(n.left)
            if nr>nl:
                mm,nm = mr,nr
            elif nr<nl:
                mm,nm = ml,nl
            else:
                mm,nm = mr+ml,nr
            if n.val in mm:
                return [n.val],nm+1
            elif nm>1:
                return mm,nm
            else:
                return mm+[n.val],1
        return mode(root)[0]
