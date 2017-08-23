class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        def gen(x):
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if x==0 and i==0: continue
                y=x*10+i
                if y <= n:
                    ret.append(y)
                    gen(y)
                else:
                    return
        gen(0)
        return ret