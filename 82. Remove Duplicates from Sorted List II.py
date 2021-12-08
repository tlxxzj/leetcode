# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        node = root
        while node and node.next and node.next.next:
            val = node.next.val
            node2 = node.next
            if node2.next.val != val:
                node = node.next
                continue
            while node2 and node2.val == val:
                node2 = node2.next
            node.next = node2
        return root.next