# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        st = [root] if root else []
        while st:
            st2 = []
            n = len(st)
            for i in range(n):
                if st[i].left:
                    st2.append(st[i].left)
                if st[i].right:
                    st2.append(st[i].right)
                if i+1<n:
                    st[i].next = st[i+1]
            st[n-1].next = None
            st = st2
        