#
# [437] Path Sum III
# 
# * Easy(39.75274%)
# * Testcase Example: '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
# * URL: https://leetcode.com/problems/path-sum-iii
# 
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ans = 0
        self.sum = sum
        self.s(root)
        return self.ans
    def s(self,node):
        if node is None:
            return []
        sums = [0] + self.s(node.left)+self.s(node.right)
        self.ans+=sums.count(self.sum-node.val)
        return [node.val+i for i in sums]
        
