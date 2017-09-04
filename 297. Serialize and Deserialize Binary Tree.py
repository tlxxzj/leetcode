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
        def preorder(l, node):
            if not node:
                l.append('#')
            else:
                l.append(str(node.val))
                preorder(l, node.left)
                preorder(l, node.right)
        
        ret = []
        preorder(ret, root)
        return ','.join(ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        n = len(data)
        i=[0]
        def preorder():
            if data[i[0]] == '#':
                i[0] += 1
                return None
            else:
                node = TreeNode(int(data[i[0]]))
                i[0] += 1
                node.left = preorder()
                node.right = preorder()
                return node
        return preorder()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))