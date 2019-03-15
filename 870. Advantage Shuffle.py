class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        A.sort()
        b = [[B[i], i, None] for i in range(n)]
        b.sort(key=lambda x: x[0])
        i = 0
        a = []
        for j in range(n):
            while i < n and A[i] <= b[j][0]:
                a.append(A[i])
                i += 1
            if i < n:
                b[j][2] = A[i]
                i += 1
        a.reverse()
        for i in range(n):
            if b[i][2] is None:
                b[i][2] = a.pop()
        b.sort(key=lambda x: x[1])
        return [b[i][2] for i in range(n)]
