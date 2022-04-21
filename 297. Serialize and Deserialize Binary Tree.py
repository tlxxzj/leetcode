# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def to_list(arr, node):
            if not node:
                arr.append('None')
                return
            arr.append(str(node.val))
            to_list(arr, node.left)
            to_list(arr, node.right)
        arr = []
        to_list(arr, root)
        return ','.join(arr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def from_list(arr):
            item = arr.pop()
            if item == 'None':
                return None
            node = TreeNode(int(item))
            node.left = from_list(arr)
            node.right = from_list(arr)
            return node
        arr = list(data.split(','))
        arr.reverse()
        return from_list(arr)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))