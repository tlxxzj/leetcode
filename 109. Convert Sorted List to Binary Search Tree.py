# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def arr2bst(a, l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(a[m])
            root.left = arr2bst(a, l, m-1)
            root.right = arr2bst(a, m+1, r)
            return root
        
        return arr2bst(arr, 0, len(arr)-1)
        