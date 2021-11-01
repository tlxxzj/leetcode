# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): return head
        r1, r2 = ListNode(0), ListNode(0)
        h1, h2 = r1, r2
        while head:
            h1.next = head
            h2.next = head.next
            h1 = h1.next
            h2 = h2.next
            head = head.next.next if head.next else None
        h1.next = r2.next
        return r1.next
        