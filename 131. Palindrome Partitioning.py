class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ispalindrome = [[True]*n for _ in range(n)]
        for j in range(n):
            for i in range(j-1, -1, -1):
                ispalindrome[i][j] = s[i] == s[j] and ispalindrome[i+1][j-1]
        
        res = []
        parts = []
        
        def dfs(i):
            if i == n:
                res.append(parts[:])
                return
            
            for j in range(i, n):
                if ispalindrome[i][j]:
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop()

        dfs(0)
        return res
                    
