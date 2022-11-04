# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        h1, h2 = root, head
        while h2:
            if h2.val == val:
                h1.next = h2.next
                h2 = h1.next
            else:
                h1, h2 = h2, h2.next
        return root.next