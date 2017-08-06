#
# [160] Intersection of Two Linked Lists
# 
# * Easy(30.51213%)
# * Testcase Example: 'No intersection: []\n[]'
# * URL: https://leetcode.com/problems/intersection-of-two-linked-lists
# 
# Write a program to find the node at which the intersection of two singly linked lists begins.
# 
# For example, the following two linked lists: 
# 
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem and creating all test cases.
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return None
        p1=headA
        p2=headB
        n1,n2=0,0
        while p1!=p2:
            if p1==None:
                p1=headB
                n1+=1
            else:
                p1=p1.next
            if p2==None:
                p2=headA
                n2+=1
            else:
                p2=p2.next
            if n1>=2 or n2>=2:
                return None
        return p1
