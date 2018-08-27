"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def visit(arr, h):
            while h:
                arr.append(Node(h.val, None, None, None))
                if len(arr) > 1:
                    arr[-2].next = arr[-1]
                    arr[-1].prev = arr[-2]
                if h.child:
                    visit(arr, h.child)
                h = h.next
        
        arr = []
        visit(arr, head)
        if head:
            return arr[0]