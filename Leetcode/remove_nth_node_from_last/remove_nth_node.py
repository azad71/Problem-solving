# first find the length
# then move pointer to length - n + 1
# remove the node and establish new link
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        if not head:
            return
        temp = head
        length = 0
        while temp.next:
            length += 1
            temp = temp.next
        if n == length+1:
            head = head.next
            return head
        
        prevNodeLen = length - n
        temp2 = head
        for _ in range(prevNodeLen):
            temp2 = temp2.next
    
        temp2.next = temp2.next.next
        return head