# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        index = {}
        lenp = len(post)
        for i in range(lenp):
            index[post[i]] = i
        def construct(pre, a, b, post, l, r):
            if a > b:
                return None
            root = TreeNode(pre[a])
            if a + 1 <= b:
                i = index[pre[a+1]]
                x = i - l
                root.left = construct(pre, a+1, a+1+x, post, l, l + x)
                root.right = construct(pre, a+1+x+1, b, post, l+x+1, r)
            return root
        return construct(pre, 0, lenp-1, post, 0, lenp-1)
