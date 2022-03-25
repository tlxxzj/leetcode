class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(i) for i in num1[::-1]]
        num2 = [int(i) for i in num2[::-1]]
        n1, n2 = len(num1), len(num2)

        num3 = [0] * (n1 + n2)
        for i in range(n1):
            k = 0
            for j in range(n2):
                k += num3[i+j] + num1[i] * num2[j]
                num3[i+j] = k%10
                k //= 10
            num3[i+n2] = k
        
        i = n1 + n2 - 1
        while i >= 0 and num3[i]==0:
            i -= 1
        if i == -1:
            return '0'
        return ''.join([str(j) for j in num3[:i+1][::-1]])
            