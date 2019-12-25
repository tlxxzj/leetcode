# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Queue:
    def __init__(self):
        self.a = []
        self.b = []

    def size(self):
        return len(self.a) + len(self.b)
    
    def push(self, x):
        self.b.append(x)

    def pop(self):
        if len(self.a) == 0:
            self.a = self.b
            self.a.reverse()
            self.b = []
        return self.a.pop()

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True
        q = Queue()
        q.push(root)
        while q.size() > 0:
            node = q.pop()
            if node.left and node.right:
                q.push(node.left)
                q.push(node.right)
            elif (not node.left) and node.right:
                return False
            elif (node.left and (not node.right)) or ((not node.left) and (not node.right)):
                if node.left and (not node.right):
                    q.push(node.left)
                while q.size() > 0:
                    node = q.pop()
                    if node.left or node.right:
                        return False
        return True