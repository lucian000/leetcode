#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator
#
# Medium (40.96%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree. 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        

    def hasNext(self):
        """
        :rtype: bool
        """
        

    def next(self):
        """
        :rtype: int
        """
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())