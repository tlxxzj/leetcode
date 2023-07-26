class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        i = 2
        s = 1
        while i * i < num:
            if num % i == 0:
                s += i
                s += num // i
            i += 1
        
        if i * i == num:
            s += i
        return s == num
                