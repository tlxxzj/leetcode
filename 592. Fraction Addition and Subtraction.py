class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            if a % b == 0:
                return b
            return gcd(b, a%b)
        
        op = ""
        nums = []
        s = expression
        n = len(s)
        i = 0
        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if op == "-":
                    num = -num
                nums.append(num)
                if op == "/":
                    b = nums.pop()
                    a = nums.pop()
                    nums.append((a, b))
            else:
                op = s[i]
                i += 1
        
        while len(nums) > 1:
            a, b = nums.pop()
            c, d = nums.pop()
            x, y = a * d + b * c, b * d
            g = gcd(abs(x), abs(y))
            x, y = x // g, y // g
            nums.append((x, y))
        
        a, b = nums[0]
        return f"{a}/{b}"
