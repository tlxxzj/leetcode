# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self._left(root)
    
    def _left(self, node):
        while node:
            self.nodes.append(node)
            node = node.left

    def next(self) -> int:
        node = self.nodes.pop()
        val = node.val
        self._left(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.nodes) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()