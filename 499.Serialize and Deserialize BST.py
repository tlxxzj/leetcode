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
        l = []
        def _tostr(node):
            if node is None:
                l.append('null')
            else:
                l.append(str(node.val))
                _tostr(node.left)
                _tostr(node.right)
        _tostr(root)
        return ','.join(l)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        pos = [0]
        def _totree():
            i = pos[0]
            pos[0] += 1
            if i >=len(l) or l[i] == 'null':
                return None
            node = TreeNode(int(l[i]))
            node.left = _totree()
            node.right = _totree()
            return node
        return _totree()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))