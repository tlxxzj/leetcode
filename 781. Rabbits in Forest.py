class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnt = 0
        count = [0] * 1000
        for i in answers:
            if i == 0:
                cnt += 1
                continue
            count[i] += 1
        for i, e in enumerate(count):
            if i== 0 or e == 0:
                continue
            cnt += ((e + i) // (i + 1)) * (i + 1)
        return cnt