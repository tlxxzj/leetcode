# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ret = []
        def toStr(node):
            if not node:
                ret.append(None)
                return
            ret.append(node.val)
            toStr(node.left)
            toStr(node.right)
        toStr(root)
        return ','.join([str(item) for item in ret])        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        items = data.split(',')
        items.reverse()
        n = len(items)
        def fromStr():
            if len(items) == 0:
                return None
            item = items.pop()
            if item == 'None':
                return None
            node = TreeNode(int(item))
            node.left = fromStr()
            node.right = fromStr()
            return node
        return fromStr()
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans