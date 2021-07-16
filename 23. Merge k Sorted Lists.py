# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        def merge(a, b):
            head = ListNode(0)
            node = head
            while a and b:
                if a.val <= b.val:
                    node.next = a
                    a = a.next
                else:
                    node.next = b
                    b = b.next
                node = node.next
            if a:
                node.next = a
            if b:
                node.next = b
            return head.next
        
        while len(lists) > 1:
            lists2 = []
            while len(lists) > 1:
                a, b = lists.pop(), lists.pop()
                lists2.append(merge(a, b))
            if len(lists) > 0:
                lists2.append(lists[0])
            lists = lists2
        return lists[0]