class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1
        
        res = 1
        s = [0] * (n + 1)
        s[:3] = [1, 2, 2]
        i, j = 2, 3
        while j < n:
            num = s[j-1] ^ 3
            if s[i] == 1:
                s[j] = num
                j += 1
            else:
                s[j] = s[j+1] = num
                j += 2
            if num == 1:
                res += s[i]
                if j > n:
                    res -= 1
            i += 1
        
        return res


            
                
