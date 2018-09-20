import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets <= 1:
            return 0
        if minutesToDie < 1:
            return 1
        
        n = buckets
        k = (minutesToTest / minutesToDie) + 1
        print k
        ret = int(math.log(n)/math.log(k))
        if k ** ret < n:
            ret += 1
        return ret
        
        