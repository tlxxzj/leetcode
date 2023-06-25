class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        res = set()
        maxl = [-1]

        rp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            if s[i] == ')':
                rp[i] = rp[i+1] + 1
            else:
                rp[i] = rp[i+1]

        def dfs(t, i, l, r):
            if l < r or l-r > rp[i]:
                return
            
            if len(t)+n-i < maxl[0]:
                return

            if i == n:
                if l != r:
                    return
                
                if len(t) > maxl[0]:
                    maxl[0] = len(t)
                    res.clear()
                res.add(t)
                return
            
            c = s[i]
            if c == '(' or c == ')':
                if c == '(':
                    dfs(t+c, i+1, l+1, r)
                else:
                    dfs(t+c, i+1, l, r+1)
                dfs(t, i+1, l, r)
            else:
                dfs(t+c, i+1, l, r)
        
        dfs("", 0, 0, 0)
        return list(res)