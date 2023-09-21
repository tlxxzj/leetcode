class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num: str) -> tuple[int, int]:
            real, imaginary = 0, 0
            i, n = 0, len(num)

            negative = False
            if num[i] == "-":
                negative = True
                i += 1
            
            while num[i] != "+":
                real = real * 10 + int(num[i])
                i += 1
            if negative:
                real = -real
            
            negative = False
            i += 1
            if num[i] == "-":
                negative = True
                i += 1
            
            while num[i] != "i":
                imaginary = imaginary * 10 + int(num[i])
                i += 1
            
            if negative:
                imaginary = -imaginary
            
            return real, imaginary
        
        x1, y1 = parse(num1)
        x2, y2 = parse(num2)
        x = x1 * x2 - y1 * y2
        y = x1 * y2 + y1 * x2
        return f"{x}+{y}i"
