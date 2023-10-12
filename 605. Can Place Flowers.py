class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 1 or (i-1>=0 and flowerbed[i-1] == 1) or (i+1<m and flowerbed[i+1] == 1):
                continue
            flowerbed[i] = 1
            n -= 1
        print(flowerbed)
        return n <= 0
