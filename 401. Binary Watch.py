class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 0 or num > 10:
            return []
        ret = []
        d = [[] for i in range(11)]
        for i in range(60):
            cnt = 0
            x = i
            while i > 0:
                cnt += 1
                i = i & (i - 1)
            d[cnt].append(x)
        for i in range(num + 1):
            a, b = i, num - i
            if a <= 4 and b <= 6:
                for h in d[a]:
                    for m in d[b]:
                        if h < 12 and m < 60:
                            s = '%d:%02d' %(h, m)
                            ret.append(s)
        
        return ret