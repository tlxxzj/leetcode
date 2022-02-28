# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def insert(root, node):
            if node.val <= root.val:
                node.next = root
                return node
            n1, n2 = root, root.next
            while n2 and node.val > n2.val:
                n1 = n1.next
                n2 = n2.next
            n1.next = node
            node.next = n2
            return root
            
        root, n1, n2 = head, head, head.next
        while n2:
            if n1.val > n2.val:
                n1.next = n2.next
                root = insert(root, n2)
                n2 = n1.next
            else:
                n1 = n1.next
                n2 = n2.next
        
        return root