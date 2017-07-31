#
# [100] Same Tree
# 
# * Easy(46.33997%)
# * Testcase Example: '[]\n[]'
# * URL: https://leetcode.com/problems/same-tree
# 
# Given two binary trees, write a function to check if they are equal or not.
# 
# 
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def eq(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val==q.val:
                return eq(p.left,q.left) and eq(p.right,q.right)
            else:
                return False
        return eq(p,q)        
