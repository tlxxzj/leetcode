# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.d = {}
        ret = self._dfs(node)
        return ret
    
    def _dfs(self, node):
        if node is None: return None
        if node in self.d:
            return self.d[node]
        newnode = UndirectedGraphNode(node.label)
        self.d[node] = newnode
        for i in node.neighbors:
            newnode.neighbors.append(self._dfs(i))
        return newnode
        
            
            
        