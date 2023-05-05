class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        m = n * n
        puzzle = [["." for j in range(n)] for i in range(n)]
        row = [0] * n
        col = [0] * n
        left = [0] * n * 2
        right = [0] * n * 2
        def dfs(step, q):
            if q == n:
                ret.append(["".join(puzzle[i]) for i in range(n)])
                return
            if step == m:
                return
            x, y = step // n, step % n
            z = row[x] + col[y] + left[x+y] + right[n-1-x+y]
            if z == 0:
                puzzle[x][y] = "Q"
                row[x] += 1
                col[y] += 1
                left[x+y] += 1
                right[n-1-x+y] += 1
                dfs(step+1, q+1)
                puzzle[x][y] = "."
                row[x] -= 1
                col[y] -= 1
                left[x+y] -= 1
                right[n-1-x+y] -= 1
            dfs(step+1, q)
        
        dfs(0, 0)

        return ret

