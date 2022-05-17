class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]
        i, j = 0, 0
        while True:
            for k in range(n-1):
                if len(strs[k]) <= j or len(strs[k+1]) <= j or strs[k][j] != strs[k+1][j]:
                    return strs[0][i:j]
            j += 1
        return strs[0][i:j]
                