class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        sum = [0] *(n + 1)

        def lowbit(x):
            return x & -x

        def update(x, v):
            while x <= n:
                sum[x] += v
                x += lowbit(x)

        def query(x):
            x=min(x, n)
            s = 0
            while x>0:
                s += sum[x]
                x -= lowbit(x)
            return s

        nums = [(nums[i], i+1) for i in range(n)]
        nums.sort()

        #print(nums)
        y = 0
        for x in range(n):
            update(nums[x][1], -1)
            while y < n and nums[y][0] - nums[x][0] <= t:
                update(nums[y][1], 1)
                y += 1
            if query(nums[x][1]+k) - query(nums[x][1]-k-1) > 0:
                return True
        return False
