class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if not key:
            return
        d = self.d
        x = None
        for c in key:
            if c in d:
                x = d[c]
                d = x[0]
            else:
                x = [{}, 0]
                d[c] = x
                d = x[0]
        x[1] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        d = self.d
        x = None
        for c in prefix:
            if c in d:
                x = d[c]
                d = x[0]
            else:
                return 0
        
        ret = 0
        q = [x]
        while len(q) > 0:
            x = q.pop()
            ret += x[1]
            for y in x[0].values():
                q.append(y)
        return ret
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)