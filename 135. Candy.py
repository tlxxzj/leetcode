class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        rank = list(range(n))
        rank.sort(key=lambda x: ratings[x])
        for i in rank:
            if i > 0 and ratings[i] > ratings[i-1]:
                candy[i] = max(candy[i], candy[i-1] + 1)
            if i < n - 1 and ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        return sum(candy)