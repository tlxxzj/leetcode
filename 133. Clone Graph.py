"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        root = node
        nodes = {node.val: node}
        newNodes = {node.val: Node(node.val)}
        q = [node]
        while len(q) > 0:
            node = q.pop()
            if not node.neighbors:
                continue
            for node in node.neighbors:
                if node.val not in nodes:
                    nodes[node.val] = node
                    newNodes[node.val] = Node(node.val)
                    q.append(node)
        for node in nodes.values():
            if not node.neighbors:
                continue
            newNode = newNodes[node.val]
            newNode.neighbors = [newNodes[neighbor.val] for neighbor in node.neighbors]
        return newNodes.get(root.val)
        
