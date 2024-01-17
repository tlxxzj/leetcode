class SummaryRanges:
    class Node:
        def __init__(self, lval, rval):
            self.lval = lval
            self.rval = rval
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def addNum(self, value: int) -> None:
        self.root = self.insert(self.root, value)

    def insert(self, node: Node, value: int):
        if node == None:
            return self.Node(value, value)
        
        if value < node.lval:
            lnode = self.insert(node.left, value)
            if lnode.rval + 1 == node.lval:
                node.lval = lnode.lval
                node.left = lnode.left
            else:
                node.left = lnode
        elif value > node.rval:
            rnode = self.insert(node.right, value)
            if rnode.lval - 1 == node.rval:
                node.rval = rnode.rval
                node.right = rnode.right
            else:
                node.right = rnode
        
        return node


    def getIntervals(self) -> List[List[int]]:
        res = []
        
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            if len(res) > 0 and res[-1][1] + 1 == node.lval:
                res[-1][1] = node.rval
            else:
                res.append([node.lval, node.rval])
            inorder(node.right)
        
        inorder(self.root)
        return res



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
