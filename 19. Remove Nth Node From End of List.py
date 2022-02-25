# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h1, h2 = head, head
        while n != 0:
            n -= 1
            h2 = h2.next
        
        if not h2:
            return head.next
        
        while h2.next:
            h1 = h1.next
            h2 = h2.next
        
        if h1.next:
            h1.next = h1.next.next
        else:
            h1.next = None
        
        return head
        