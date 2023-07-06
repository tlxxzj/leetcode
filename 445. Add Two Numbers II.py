# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        while h1 and h2:
            h1, h2 = h1.next, h2.next
        
        res = [0]
        while h1:
            res.append(l1.val)
            h1, l1 = h1.next, l1.next
        
        while h2:
            res.append(l2.val)
            h2, l2 = h2.next, l2.next
        
        while l1:
            res.append(l1.val + l2.val)
            l1, l2 = l1.next, l2.next
        
        res.reverse()
        n = len(res)
        for i in range(n-1):
            if res[i] > 9:
                res[i+1] += 1
                res[i] = res[i] % 10
        
        if res[-1] == 0:
            res.pop()
        h = None
        for num in res:
            h = ListNode(num, h)
        
        return h
