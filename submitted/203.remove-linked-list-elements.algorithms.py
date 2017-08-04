#
# [203] Remove Linked List Elements
# 
# * Easy(32.2295%)
# * Testcase Example: '[1,2,6,3,4,5,6]\n6'
# * URL: https://leetcode.com/problems/remove-linked-list-elements
# 
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = ListNode(val)
        pre.next = head
        p=pre
        while p.next:
            if p.next.val==val:
                p.next = p.next.next
            else:
                p=p.next
        return pre.next
