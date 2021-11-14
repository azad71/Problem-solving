"""
Link -> https://leetcode.com/problems/delete-node-in-a-linked-list/
Tag -> Singly Linked List
"""
class Solution(object):
    def deleteNode(self, node):
        # say a list is 1 -> 2 -> 3 -> 4, we are deleting 2
        # set node(2) value to 3, now node.val = 3
        # point node.next to 4, now list is 1 -> 3 -> 4
        node.val = node.next.val
        node.next = node.next.next