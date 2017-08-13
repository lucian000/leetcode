#
# [234] Palindrome Linked List
# 
# * Easy(32.57115%)
# * Testcase Example: '[]'
# * URL: https://leetcode.com/problems/palindrome-linked-list
# 
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        nxt = slow.next
        slow.next = None
        while nxt:
            slow,nxt,node = nxt,nxt.next,slow
            slow.next = node
        while slow and head:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
