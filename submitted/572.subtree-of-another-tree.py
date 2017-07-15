#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree
#
# Easy (41.00%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(a,b):
            if a==None and b==None:
                return True
            if a==None or b==None:
                return False
            if a.val==b.val and check(a.left,b.left) and check(a.right, b.right):
                return True
            return False
        def subcheck(s,t):
            if s==None:
                return False
            if check(s,t):
                return True
            if subcheck(s.left,t) or subcheck(s.right,t):
                return True
        if subcheck(s,t) in [None,False]:
            return False
        else:
            return True
