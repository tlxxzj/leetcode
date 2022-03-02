# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        
        ret = head.next
        left, right = None, head
        while right:
            n1, n2 = right, right.next
            if n2:
                if left:
                    left.next = n2
                left = n1
                right = n2.next
                n1.next = None
                n2.next = n1
            else:
                left.next = n1
                break
        
        return ret
        
        