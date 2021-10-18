"""
Link -> https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Tag -> Singly Linked List
"""

# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        ptr = head
        
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        
        return head