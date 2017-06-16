class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.sums = [0] *  (self.n * 4)
        if self.n > 0:
            self.init_sums(1, 0, self.n-1, nums)
    
    def init_sums(self, root, l, r, nums):
        if l == r:
            self.sums[root] = nums[l]
        else:
            m = (l + r) / 2
            self.init_sums(root<<1, l, m, nums)
            self.init_sums(root<<1|1, m+1, r, nums)
            self.sums[root] = self.sums[root<<1] + self.sums[root<<1|1]
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self._update(1, 0, self.n-1, i, val)
    
    def _update(self, root, l, r, i, val):
        if l == r:
            self.sums[root] = val
        else:
            m = (l + r) / 2
            if i <= m:
                self._update(root<<1, l, m, i, val)
            else:
                self._update(root<<1|1, m+1, r, i, val)
            self.sums[root] = self.sums[root<<1] + self.sums[root<<1|1]

        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._query(1, 0, self.n-1, i, j)
    
    def _query(self, root, l, r, i, j):
        if l>=i and r <=j:
            return self.sums[root]
        if l>j or r < i:
            return 0
        m = (l + r) / 2
        return self._query(root<<1, l, m, i, j) + self._query(root<<1|1, m+1, r, i, j)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)