"""
Link -> https://leetcode.com/problems/middle-of-the-linked-list/
Tag -> Singly Linked List
"""

# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def middleNode(self, head):
        oneStep = head
        twoStep = head
        
        if not head.next:
            return head
        while twoStep and twoStep.next:
            oneStep = oneStep.next
            twoStep = twoStep.next.next
        
        return oneStep