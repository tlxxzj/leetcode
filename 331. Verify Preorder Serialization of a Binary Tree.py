class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        nodes.reverse()
        n = len(nodes)
        if (n - 1) % 2 != 0:
            return False
        
        def isValid():
            if len(nodes) == 0:
                return False
            if nodes.pop() == '#':
                return True
            return isValid() and isValid()
        
        return isValid() and len(nodes) == 0
            
        