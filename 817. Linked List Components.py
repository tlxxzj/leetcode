# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        nums2 = set()
        nodes = {}
        h = head
        while h:
            nodes[h.val] = h
            h = h.next
        
        h = head
        ret = 0
        while h:
            num = h.val
            h = h.next
            if (num not in nums) or (num in nums2):
                continue
            ret += 1
            node = nodes[num]
            while node and node.val in nums:
                nums2.add(node.val)
                node = node.next
        return ret
