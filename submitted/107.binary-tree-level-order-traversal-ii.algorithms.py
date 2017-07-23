#
# [107] Binary Tree Level Order Traversal II
# 
# * Easy(39.86%)
# * Testcase Example: '[3,9,20,null,null,15,7]'
# * URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii
# 
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans={}
        def addans(node,n):
            if node==None:
                return
            if n in ans:
                ans[n].append(node.val)
            else:
                ans[n] = [node.val]
            addans(node.left,n+1)
            addans(node.right,n+1)
        addans(root,0)
        n = len(ans)-1
        return [ans[i] for i in range(n,-1,-1)]
            
