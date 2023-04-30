class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [False] * (n + 1)
        q = [0]
        while len(q) >0:
            start = q.pop()
            for i in range(start+1, min(n+1, start+20)):
                if s[start:i] in wordDict and (not dp[i]):
                    dp[i] = True
                    q.append(i)
        return dp[n]
