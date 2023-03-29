"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct_node(x1, y1, x2, y2) -> Node | int:
            if x2 - x1 == 1 or y2 - y1 == 1:
                return grid[x1][y1]
            x0 = (x1 + x2) // 2
            y0 = (y1 + y2) // 2
            topLeft = construct_node(x1, y1, x0, y0)
            topRight = construct_node(x1, y0, x0, y2)
            bottomLeft = construct_node(x0, y1, x2, y0)
            bottomRight = construct_node(x0, y0, x2, y2)
            if topLeft == topRight == bottomLeft == bottomRight:
                return topLeft
            
            nodes = [topLeft, topRight, bottomLeft, bottomRight]
            for i in range(4):
                if not isinstance(nodes[i], Node):
                    nodes[i] = Node(nodes[i], True, None, None, None, None)
            
            return Node(1, False, *nodes)
        
        n = len(grid)
        node = construct_node(0, 0, n, n)
        if not isinstance(node, Node):
            node = Node(node, True, None, None, None, None)
        return node
