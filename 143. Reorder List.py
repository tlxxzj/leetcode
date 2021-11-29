# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        i, j = 0, n-1
        while i < j:
            nodes[i].next = nodes[j]
            nodes[j].next = nodes[i+1]
            i = i + 1
            j = j - 1
        nodes[i].next = None
        return nodes[0]