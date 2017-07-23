#
# [83] Remove Duplicates from Sorted List
# 
# * Easy(39.7393%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list
# 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def rmd(node):
            if node==None:
                return None
            if node.next==None:
                return node
            if node.val == node.next.val:
                return rmd(node.next)
            else:
                node.next = rmd(node.next)
                return node
        return rmd(head) 
