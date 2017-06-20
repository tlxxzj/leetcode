class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self._dfs(n, 9, k, [])
        return self.ret
    
    def _dfs(self, n, d, k, l):
        if k == 0 and n == 0:
            self.ret.append(l[:])
            return
        if n <= 0 or d == 0 or k == 0:
            return
        self._dfs(n, d-1, k, l)
        l.append(d)
        self._dfs(n-d, d-1, k-1, l)
        l.pop()        


