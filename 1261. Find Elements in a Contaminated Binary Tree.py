# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.nodes = set()
        root.val = 0
        q = [root]
        while len(q) > 0:
            x = q.pop()
            self.nodes.add(x.val)
            if x.left:
                x.left.val = 2 * x.val + 1
                q.append(x.left)
            if x.right:
                x.right.val = 2 * x.val + 2
                q.append(x.right)

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)