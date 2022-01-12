# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def buildMaxTree(nums, l, r):
            if l > r:
                return None
            m = l
            for i in range(l+1, r+1):
                if nums[i] > nums[m]:
                    m = i
            node = TreeNode(nums[m])
            node.left = buildMaxTree(nums, l, m-1)
            node.right = buildMaxTree(nums,m+1, r)
            return node
        return buildMaxTree(nums, 0, len(nums)-1)