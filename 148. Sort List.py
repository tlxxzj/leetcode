# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        a, b = head, head.next
        while b and b.next:
            a, b = a.next, b.next.next
        b = a.next
        a.next = None
        a = head
        a, b = self.sortList(a), self.sortList(b)
        root = ListNode(0)
        tail = root
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        while a:
            tail.next = a
            a = a.next
            tail = tail.next
        while b:
            tail.next = b
            b = b.next
            tail = tail.next
        return root.next

        