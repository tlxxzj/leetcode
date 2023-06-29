class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        
        def dfs(a, b, i):
            if i == n:
                return True
            
            c = str(a+b)
            if num[i:].startswith(c):
                return dfs(b, a+b, i+len(c))
            return False
        
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            for j in range(i+1, n):
                if num[i] == '0' and j-i>1:
                    break
                if dfs(int(num[:i]), int(num[i:j]), j):
                    return True
        return False