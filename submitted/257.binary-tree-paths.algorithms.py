#
# [257] Binary Tree Paths
# 
# * Easy(37.95988%)
# * Testcase Example: '[1,2,3,null,5]'
# * URL: https://leetcode.com/problems/binary-tree-paths
# 
# Given a binary tree, return all root-to-leaf paths.
# 
# 
# For example, given the following binary tree:
# 
# 
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# 
# 
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        def path(n):
            if n.left is None and n.right is None:
                return [[n.val]]
            if n.left is None:
                return [[n.val]+i for i in path(n.right)]
            if n.right is None:
                return [[n.val]+i for i in path(n.left)]
            return [[n.val]+i for i in path(n.left)+path(n.right)]
        ans = path(root)
        return ['->'.join([str(j) for j in i]) for i in path(root)]
