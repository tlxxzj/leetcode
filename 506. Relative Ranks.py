class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def genRank(i):
            if i == 1:
                return "Gold Medal"
            elif i == 2:
                return "Silver Medal"
            elif i == 3:
                return "Bronze Medal"
            return str(i)
        
        n = len(score)
        rank = [[score[i], i] for i in range(n)]
        rank.sort(key=lambda x: x[0], reverse=True)
        for i in range(n):
            rank[i][0] = genRank(i+1)
        
        rank.sort(key=lambda x: x[1])
        return [r for r, i in rank]
