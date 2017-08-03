#
# [235] Lowest Common Ancestor of a Binary Search Tree
# 
# * Easy(38.87914%)
# * Testcase Example: '[2,1]\nnode with value 2\nnode with value 1'
# * URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# 
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# 
# 
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
# 
# 
# 
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# 
# 
# 
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p=p
        self.q=q
        self.ans=None
        self.search(root)
        return self.ans
    def search(self,n):
        if not n:
            return 0
        a=self.search(n.left)
        b=self.search(n.right)
        if self.ans:
            return
        s= sum((n==self.p,n==self.q,a,b))
        if s==2:
            self.ans=n
            return
        return s
            
