class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ret = []
        for a in asteroids:
            if len(ret) == 0 or a > 0 or ret[-1] < 0:
                ret.append(a)
            else:
                while len(ret) > 0 and ret[-1] > 0 and abs(a) > ret[-1]:
                    ret.pop()
                if len(ret) > 0 and ret[-1] == abs(a):
                    ret.pop()
                elif len(ret) == 0 or ret[-1] < 0:
                    ret.append(a)
        return ret