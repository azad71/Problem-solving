"""
Link https://leetcode.com/problems/add-two-numbers/
Tag -> Singly Linked List
"""

# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        carry = 0
        ptr = result
        
        while l1 or l2 or carry:
            d1 = 0
            d2 = 0
            sum = 0
            
            if l1 and l1.val:
                d1 = l1.val
            if l2 and l2.val:
                d2 = l2.val
            
            sum = d1 + d2 + carry
            carry = sum // 10
            sum = sum % 10
            ptr.next = ListNode(sum)
            ptr = ptr.next
            
            
            if l1 and l1.next:
                l1 = l1.next
            else:
                l1 = None
            
            
            if l2 and l2.next:
                l2 = l2.next
            else:
                l2 = None
                
        return result.next