"""
Link -> https://leetcode.com/problems/reverse-linked-list/
Tag -> Singly Linked List
"""

# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def reverseList(self, head):
        # checks for empty list
        if not head:
            return
        
        # if list had only one element
        if not head.next:
            return head
        
        # getting first node on new list
        temp = ListNode(head.val)
        head = head.next
        while head.next:
            newNode = ListNode(head.val)
            newNode.next = temp
            temp = newNode
            head = head.next
        head.next = temp
        return head