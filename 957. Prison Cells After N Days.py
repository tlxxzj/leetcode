class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        def cells2int(cs):
            ret = 0
            for i in range(8):
                ret += cs[i] * (1 << i)
            return ret
        
        def int2cells(num):
            cs = [0] * 8
            for i in range(8):
                if num & (1<<i) > 0:
                    cs[i] = 1
            return cs

        ci = cells2int(cells)
        status = set([ci])
        status2 = [ci]
        while 1:
            cells2 = list(cells)
            cells2[0] = cells2[-1] = 0
            for i in range(1, 7):
                if cells[i-1] + cells[i+1] in [0, 2]:
                    cells2[i] = 1
                else:
                    cells2[i] = 0
            if len(status) == N:
                return cells2
            ci = cells2int(cells2)
            if ci in status:
                i = status2.index(ci)
                status2 = status2[i:]
                N -= i
                break
            status.add(ci)
            status2.append(ci)
            cells = cells2
        
        ci = status2[N%len(status2)]
        return int2cells(ci)