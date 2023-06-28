class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ispalindrome = [[False]*n for _ in range(n)]
        dp = [[set() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i,n):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                ispalindrome[i][j] = l >= r
                if ispalindrome[i][j]:
                    dp[i][j].add((s[i:j+1], ))

        for k in range(1, n):
            for i in range(n-k):
                l, r = i, i+k
                for j in range(k):
                    m = i+j
                    for left in dp[l][m]:
                        for right in dp[m+1][r]:
                            dp[l][r].add(left+right)
        return list(dp[0][n-1])
                    
