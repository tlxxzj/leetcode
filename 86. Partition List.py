# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        r1 = ListNode(0)
        r2 = ListNode(0)
        h1 = r1
        h2 = r2
        cnt = 0
        while head:
            if head.val < x:
                h1.next = head
                h1 = h1.next
            else:
                h2.next = head
                h2 = h2.next 
            head = head.next
        h1.next = r2.next
        h2.next = None
        return r1.next