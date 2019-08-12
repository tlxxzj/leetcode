class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def get_f(val):
            if val <= 1:
                return val
            n = 1
            while (2 ** n) - 1 < val:
                n += 1
            
            n_end = (2 ** n) - 1
            n_begin = n_end - (2 ** (n - 1)) + 1
            
            return (n_end - (val - n_begin)) // 2
        
        ret = [label]
        while ret[-1] != 1:
            ret.append(get_f(ret[-1]))
        ret.reverse()
        return ret
        
            