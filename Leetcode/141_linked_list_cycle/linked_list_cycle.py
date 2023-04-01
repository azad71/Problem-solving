"""
Link -> https://leetcode.com/problems/linked-list-cycle/
Tag -> Singly Linked List, Floyd Cycle Detection
"""

# Node class
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        hare = head
        tortoise = head

        
        if not head:
            return False
        
        if not head.next:
            return False
        
        while hare:
            if hare.next and hare.next.next:
                hare = hare.next.next
            else:
                return False
            tortoise = tortoise.next
            
            if hare == tortoise:
                return True
        