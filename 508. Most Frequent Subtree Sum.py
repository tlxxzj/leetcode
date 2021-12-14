# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        def find(node):
            if not node:
                return 0
            s = node.val + find(node.left) + find(node.right)
            freq[s] += 1
            return s
        
        find(root)
        maxFreq = max(freq.values())
        return [k for k, v in filter(lambda x: x[1] == maxFreq, freq.items())]
