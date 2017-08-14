#
# [538] Convert BST to Greater Tree
# 
# * Easy(51.89284%)
# * Testcase Example: '[5,2,13]'
# * URL: https://leetcode.com/problems/convert-bst-to-greater-tree
# 
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# 
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.vals = []
        self.read(root)
        self.sum = 0
        self.store(root)
        return root
    def read(self,root):
        if root:
            self.read(root.left)
            self.vals.append(root.val)
            self.read(root.right)
    def store(self,root):
        if root:
            self.store(root.right)
            self.sum += self.vals.pop()
            root.val = self.sum
            self.store(root.left)
