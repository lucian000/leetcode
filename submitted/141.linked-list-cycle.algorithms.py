#
# [141] Linked List Cycle
# 
# * Easy(35.39824%)
# * Testcase Example: '[]\nno cycle'
# * URL: https://leetcode.com/problems/linked-list-cycle
# 
# Given a linked list, determine if it has a cycle in it.
# 
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        n1 = head
        n2 = head.next
        while n1!=n2:
            if n2.next==None or n2.next.next==None:
                return False
            n1=n1.next
            n2=n2.next.next
        return True
