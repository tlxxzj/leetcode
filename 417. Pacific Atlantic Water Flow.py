class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def search(edges):
            visited = set()
            def dfs(x, y):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x2 = x + dx
                    y2 = y + dy
                    if x2 <0 or x2>= m or y2<0 or y2>= n or heights[x2][y2] < heights[x][y]:
                        continue
                    dfs(x2, y2)
            for x, y in edges:
                dfs(x, y)
            return visited
        
        pacific = search([(i, 0) for i in range(m)] + [(0, i) for i in range(n)])
        atlantic = search([(i, n-1) for i in range(m)] + [(m-1, i) for i in range(n)])
        return list(search(pacific) & search(atlantic))

        return ret

                
                
        


        
