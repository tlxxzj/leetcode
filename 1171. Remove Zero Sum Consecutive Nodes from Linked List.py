# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def list2arr(node):
            arr = []
            while node:
                arr.append(node.val)
                node = node.next
            return arr
        
        def arr2list(arr):
            head = ListNode(0)
            h = head
            for i in arr:
                h.next = ListNode(i)
                h = h.next
            return head.next
        
        arr = list2arr(head)
        n = len(arr)
        s = [0] * n
        s[0] = arr[0]
        index = {s[0]: [0]}
        for i in range(1, n):
            s[i] = s[i-1] + arr[i]
            if s[i] in index:
                index[s[i]].append(i)
            else:
                index[s[i]] = [i]
        
        print(s)
        arr2 = []
        i = max(index.get(0, [-1])) + 1
        while i < n:
            if arr[i] == 0:
                i += 1
                continue
            j = max(index.get(s[i], [0]))
            arr2.append(arr[i])
            if i < j:
                i = j + 1
            else:
                i += 1
        
        return arr2list(arr2)
        
        
        
        