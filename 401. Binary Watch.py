class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        def bitCount(h, m):
            count = 0
            while h>0:
                count+=1
                h -= -h&h
            while m > 0:
                count+=1
                m -= -m&m
            return count

        for h in range(12):
            for m in range(60):
                if bitCount(h, m) == turnedOn:
                    ret.append("{h}:{m:02d}".format(h=h,m=m))
        
        return ret