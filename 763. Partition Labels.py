class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        count = {}
        for c in S:
            count[c] = count.get(c, 0) + 1
        
        ret = []
        x = 0
        lasti = -1
        for i in range(len(S)):
            c = S[i]
            x += count[c]
            count[c] = 0
            x -= 1
            if x == 0:
                ret.append(i-lasti)
                lasti = i
        return ret
        