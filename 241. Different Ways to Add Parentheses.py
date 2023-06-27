class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        if n == 0:
            return []
        dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

        def dfs(l, r):
            if len(dp[l][r]) > 0:
                return
            if expression[l:r].isdigit():
                dp[l][r].append(int(expression[l:r]))
                return
            
            for i in range(l, r):
                if expression[i] in "+-*":
                    dfs(l, i)
                    dfs(i+1, r)
                    for x in dp[l][i]:
                        for y in dp[i+1][r]:
                            if expression[i] == "+":
                                dp[l][r].append(x+y)
                            elif expression[i] == "-":
                                dp[l][r].append(x-y)
                            else:
                                dp[l][r].append(x*y)

        dfs(0, n)
        return list(dp[0][n])
