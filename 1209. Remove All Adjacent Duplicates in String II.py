class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        q = ['']
        x = 1
        for c in s:
            q.append(c)
            if q[-1] == q[-2]:
                x += 1
            else:
                x = 1
            while x == k:
                q = q[:-k]
                x = 1
                while x < len(q) and x < k and q[-1] == q[-(x+1)]:
                    x+=1
        return ''.join(q[1:])