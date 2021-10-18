"""
Link -> https://leetcode.com/problems/merge-two-sorted-lists/
Tag -> Singly Linked List
"""

# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        
        mergedList = ListNode()
        ptr = mergedList
        
        while l1 and l2:
            if l1.val >= l2.val:
                # value of second list goes in
                newNode = ListNode(l2.val)
                ptr.next = newNode
                l2 = l2.next
                del newNode
            else:
                # value of first list goes in
                newNode = ListNode(l1.val)
                l1 = l1.next
                ptr.next = newNode
                del newNode
            # update the tail pointer
            ptr = ptr.next
            
        if l2:
            ptr.next = l2
        else:
            ptr.next = l1
            
        mergedList = mergedList.next
            
        # mergedList holds the initial memory location of ptr
        return mergedList
        