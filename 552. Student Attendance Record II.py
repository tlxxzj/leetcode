class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 1000000007
        class Node:
            def __init__(self):
                self.a0=0
                self.a1=0
                self.a2=0
                self.l0=0
                self.l1=0
                self.l2=0
        a, b = Node(), Node()
        a.l0=1
        for i in xrange(1, n+1):
            a, b = b, a
            a.l0 = (b.l0 + b.l1 + b.l2) % mod
            a.l1 = b.l0
            a.l2 = b.l1
            
            a.a0 = (b.a0 + b.a1 + b.a2 + b.l0 + b.l1 + b.l2) % mod
            a.a1 = b.a0
            a.a2 = b.a1
        
        x=a
        return (x.a0 + x.a1 + x.a2 + x.l0 + x.l1 + x.l2) % mod
            
            
            
            
            