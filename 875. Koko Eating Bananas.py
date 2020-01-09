class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        ret = 0
        s = sum(piles)
        while low <= high:
            k = (low + high) >> 1
            k1 = k - 1
            if (s + k1) // k > H:
                low = k + 1
                continue
            h = 0
            for p in piles:
                h += (p + k1) // k
                if h > H: break
            if h > H:
                low = k + 1
            else:
                high = k - 1
                ret = k
        return ret