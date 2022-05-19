# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        h = root
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
        while l1:
            h.next = l1
            l1 = l1.next
            h = h.next
        while l2:
            h.next = l2
            l2 = l2.next
            h = h.next
        return root.next
            