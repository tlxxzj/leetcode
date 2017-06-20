class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.arr = candidates
        self._dfs(len(candidates)-1, target, [])
        return self.ret
    
    def _dfs(self, i, sum, l):
        if sum == 0:
            self.ret.append(l[:])
            return
        if i < 0 or sum < 0:
            return
        self._dfs(i-1, sum, l)
        for k in range(sum/self.arr[i]):
            l.append(self.arr[i])
            self._dfs(i-1, sum-(k+1)*self.arr[i], l)
        for k in range(sum/self.arr[i]):
            l.pop()