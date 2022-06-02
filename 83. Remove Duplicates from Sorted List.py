# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head
        while head:
            node = head.next
            while node and node.val == head.val:
                node = node.next
            head.next = node
            head = head.next
        return root