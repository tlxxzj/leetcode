class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        b = 31
        B = 1
        for i in range(10):
            B *= b
        h = 0
        for c in s[:10]:
            h = h * b + ord(c)
        d = {
            h: [9]
        }
        ret = set()
        for i, c in enumerate(s[10:], 10):
            h = h * b + ord(c) - ord(s[i-10]) * B
            x = h
            #print x
            if x in d:
                f = False
                for y in d[x]:
                    if s[y - 9: y + 1] == s[i - 9: i + 1]:
                        f = True
                        ret.add(y)
                        break
                if not f:
                    d[x].append(i)
            else:
                d[x] = [i]
        return [s[i - 9: i + 1] for i in ret]
        