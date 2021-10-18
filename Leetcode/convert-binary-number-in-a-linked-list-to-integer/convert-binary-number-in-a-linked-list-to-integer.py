"""
Link -> https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Tag -> Singly Linked List
"""

# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        
        binString = ""
        while head:
            binString += str(head.val)
            head = head.next
        
        return int(binString, 2)