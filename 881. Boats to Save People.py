class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n <= 1:
            return n
        people.sort()
        ret = 0
        i, j = 0, n - 1
        while i <= j:
            while j > i and people[i] + people[j] > limit:
                j -= 1
                ret += 1
            if j > i and people[i] + people[j] <= limit:
                j -= 1
            ret += 1
            i += 1
        return ret
