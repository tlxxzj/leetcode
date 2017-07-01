class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        vis = [[False for j in range(n)] for i in range(m)]
        def dfs(i, j, k):
            if i <0 or i >=m or j<0 or j>=n or vis[i][j] or board[i][j]!=word[k]:
                return False
            k+=1
            if k == len(word):
                return True
            vis[i][j] = True
            if dfs(i-1, j, k) or dfs(i+1, j, k) or dfs(i, j-1, k) or dfs(i, j+1, k):
                return True
            vis[i][j] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
        
        