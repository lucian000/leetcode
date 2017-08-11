#
# [653] Two Sum IV - Input is a BST
# 
# * Easy(51.46624%)
# * Testcase Example: '[5,3,6,2,4,null,7]\n9'
# * URL: https://leetcode.com/problems/two-sum-iv-input-is-a-bst
# 
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
# 
# Example 1:
# 
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# Target = 9
# 
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# Target = 28
# 
# Output: False
# 
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.alllist = []
        self.ans = False
        def add(n):
            for i in self.alllist:
                if i+n==k:
                    self.ans=True
                    return
            self.alllist.append(n)
        def listall(node):
            if self.ans:
                return
            if node is None:
                return
            add(node.val)
            if self.ans:
                return
            listall(node.left)
            listall(node.right)
        listall(root)
        return self.ans
            
