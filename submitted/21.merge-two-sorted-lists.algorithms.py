#
# [21] Merge Two Sorted Lists
# 
# * Easy(38.98157%)
# * Testcase Example: '[]\n[]'
# * URL: https://leetcode.com/problems/merge-two-sorted-lists
# 
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def merge(l1,l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val>l2.val:
                l2.next = merge(l1,l2.next)
                return l2
            else:
                l1.next = merge(l2,l1.next)
                return l1
        return merge(l1,l2)  
