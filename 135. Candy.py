class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        l, r = [1] * n, [1] * n
        for i in range(n - 1):
            a, b = i + 1, n - i - 2
            if ratings[a] > ratings[a - 1]:
                l[a] = l[a - 1] + 1
            if ratings[b] > ratings[b + 1]:
                r[b] = r[b + 1] + 1
        x = [max(l[i], r[i]) for i in range(n)]
        #print l
        #print r
        #print x
        ret = sum(x)
        return ret
        