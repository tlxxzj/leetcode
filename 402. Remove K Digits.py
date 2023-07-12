class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = []
        for digit in num:
            while k > 0 and len(q) > 0 and int(digit) < int(q[-1]):
                q.pop()
                k -= 1
            q.append(digit)
        
        l, r = 0, len(q) - k
        while l < len(q) and q[l] == "0":
            l+=1
    
        if l >= r:
            return "0"
        return "".join(q[l:r])