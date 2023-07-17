class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        m, n = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        i, j, k = 0, 0, 0
        while i < m or j < n:
            a, b = 0, 0
            if i < m:
                a = int(num1[i])
            if j < n:
                b = int(num2[j])
            k = k + a + b
            res.append(str(k % 10))
            k = k // 10
            i, j = i+1, j+1
        
        if k >0:
            res.append(str(k))
        
        return "".join(res[::-1])
