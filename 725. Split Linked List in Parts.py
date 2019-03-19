# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ret = []
        n = 0
        r = root
        while r:
            n += 1
            r = r.next
        if k >= n:
            ret = [None for i in range(k)]
            for i in range(n):
                ret[i] = root
                root = root.next
                ret[i].next = None
            return ret
        for i in range(k):
            pre = root
            ret.append(root)
            if i < n%k:
                root = root.next
            for j in range(n//k):
                pre = root
                root = root.next
            pre.next = None
        
        return ret