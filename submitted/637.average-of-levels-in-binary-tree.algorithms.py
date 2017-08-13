#
# [637] Average of Levels in Binary Tree
# 
# * Easy(58.49172%)
# * Testcase Example: '[3,9,20,15,7]'
# * URL: https://leetcode.com/problems/average-of-levels-in-binary-tree
# 
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# 
# Example 1:
# 
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# 
# 
# 
# Note:
# 
# The range of node's value is in the range of 32-bit signed integer.
# 
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        return [float(sum(i))/len(i) for i in self.ns(root)]
    def ns(self, node):
        if node.left is None and node.right is None:
            return [[node.val]]
        if node.left is None:
            return [[node.val]]+self.ns(node.right)
        if node.right is None:
            return [[node.val]]+self.ns(node.left)
        return [[node.val]] + self.combine(self.ns(node.left),self.ns(node.right))
    def combine(self,a,b):
        if len(a)>len(b):
            a,b = b,a
        for i,ai in enumerate(a):
            b[i].extend(ai)
        return b
