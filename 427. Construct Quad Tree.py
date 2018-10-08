"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        
        def isLeaf(g, x, y, x2, y2):
            for i in range(x, x2):
                for j in range(y, y2):
                    if g[i][j] != g[x][y]:
                        return False
            return True
        
        def visit(g, x, y, x2, y2):
            val = '*'
            if g[x][y]:
                val = True
            else:
                val = False
            n = x2 - x
            if n == 1 or isLeaf(g, x, y, x2, y2):
                return Node(val, True, None, None, None, None)
            else:
                topLeft = visit(g, x, y, (x+x2)/2, (y+y2)/2)
                topRight = visit(g, x, (y+y2)/2, (x+x2)/2, y2)
                bottomLeft = visit(g, (x+x2)/2, y, x2, (y+y2)/2)
                bottomRight = visit(g, (x+x2)/2, (y+y2)/2, x2, y2)
                return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        n = len(grid)
        return visit(grid, 0, 0, n, n)
                
                
        
        
        