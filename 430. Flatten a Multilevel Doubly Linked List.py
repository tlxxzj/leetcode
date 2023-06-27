"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flat(node):
            if not node:
                return None, None
            
            tail = node
            while True:
                if tail.child:
                    child, childt = flat(tail.child)
                    if tail.next:
                        childt.next, tail.next.prev = tail.next, childt
                    tail.next, child.prev = child, tail
                    tail.child = None
                    tail = childt
                if tail.next:
                    tail = tail.next
                else:
                    break

            return node, tail
        
        h, t = flat(head)
        return h