class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        sq = int(math.sqrt(area))
        for i in range(sq, 0, -1):
            if area % i == 0:
                return sorted([i, area/i], reverse=True)
        return [area, 1]
        