"""
Link -> https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Tag -> Singly Linked List
"""

# two pointer approach
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = ListNode(0, head)
        # set left and right pointer
        leftPtr = temp
        rightPtr = head
        
        # move right pointer to nth position first
        while n > 0 and rightPtr:
            rightPtr = rightPtr.next
            n -= 1
    
        # now move both pointer till right pointer hits end
        while rightPtr:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next
        
        # now left pointer at one node behind nth node
        # remove the link and set new link
        leftPtr.next = leftPtr.next.next
        
        return temp.next