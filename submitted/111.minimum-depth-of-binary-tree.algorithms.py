#
# [111] Minimum Depth of Binary Tree
# 
# * Easy(33.01165%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/minimum-depth-of-binary-tree
# 
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans=1
        nodes=[root]
        while True:
            new = []
            for n in nodes:
                if n:
                    if n.left is None and n.right is None:
                        return ans
                    new.append(n.left)
                    new.append(n.right)
            nodes=new
            ans+=1
