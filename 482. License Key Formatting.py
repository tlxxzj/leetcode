class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        m = n % k
        res = []
        if m > 0:
            res.append(s[:m])
        i=m
        while i < n:
            res.append(s[i:i+k])
            i+=k
        return "-".join(res)
