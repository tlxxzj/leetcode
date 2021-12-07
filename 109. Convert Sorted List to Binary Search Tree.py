# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        def toBST(i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(nodes[i].val)
            k = (i + j) // 2
            root = TreeNode(nodes[k].val)
            root.left = toBST(i, k-1)
            root.right = toBST(k+1, j)
            return root
        return toBST(0, len(nodes)-1)
