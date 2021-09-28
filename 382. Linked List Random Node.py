# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self._head = head
        self._n = 0
        while head:
            self._n += 1
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        from random import randint
        r = randint(0, self._n - 1)
        h = self._head
        while r > 0:
            r -= 1
            h = h.next
        return h.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()