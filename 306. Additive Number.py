class Solution:
    def startswith(self, s, s2, start=0):
        l1, l2 = len(s), len(s2)
        if l1 - start < l2:
            return False
        i = 0
        while i + start < l1 and i < l2 and s[i+start] == s2[i]:
            i += 1
        return i == l2

    def is_additive(self, num, i, j):
        n = len(num)
        k = -1
        while j < n:
            if (num[k+1] == '0' and i-k >1) or (num[i+1] == '0' and j-i>1):
                return False
            a, b = int(num[k+1:i+1]), int(num[i+1:j+1])
            c = a + b
            cs = str(c)
            k = j + len(cs)
            if not self.startswith(num, cs, j+1):
                return False
            i, j, k = j, k, i
            if j == n - 1:
                break
        return j == n - 1

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        
        for i in range(n):
            for j in range(i+1, n):
                if self.is_additive(num, i, j):
                    return True
        return False