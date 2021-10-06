# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        nodes = [root] if root else []
        if root:
            root.val = 0
        self._node_set = set()
        while len(nodes) > 0:
            node = nodes.pop()
            self._node_set.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                nodes.append(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                nodes.append(node.right)

    def find(self, target: int) -> bool:
        return target in self._node_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)