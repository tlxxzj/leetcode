class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for n in range(1, numRows):
            row = [1] * (n + 1)
            for i in range(1, n):
                row[i] = ret[-1][i-1] + ret[-1][i]
            ret.append(row)
        return ret
