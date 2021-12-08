# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        root = ListNode(0, head)
        i = 0
        preNode = None
        node = root
        l1, l2 = None, None
        while node:
            if i == left:
                l1, l2 = preNode, node
            elif i == right:
                l1.next = node
                l2.next = node.next
            nextNode = node.next
            if left < i <= right:
                node.next = preNode
            preNode = node
            node = nextNode
            i += 1
        return root.next
        
