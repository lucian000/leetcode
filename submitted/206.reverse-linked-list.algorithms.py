#
# [206] Reverse Linked List
# 
# * Easy(45.20213%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/reverse-linked-list
# 
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        node,nxt = head,head.next
        node.next = None
        while nxt:
            node,nxt,pre = nxt,nxt.next,node
            node.next = pre
        return node
