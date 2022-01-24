# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        h = head
        tail = h
        while h:
            tail = h
            n += 1
            h = h.next
        k = k % n
        if k == 0:
            return head
        
        tail.next = head
        m = n - k - 1
        h = head
        while m > 0:
            m -= 1
            h = h.next
        head = h.next
        h.next = None
        return head
        
