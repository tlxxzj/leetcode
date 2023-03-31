class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        from functools import cmp_to_key
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            return a[1] - b[1]
        
        people.sort(key=cmp_to_key(cmp))
        people.reverse()
        n = len(people)
        ret = [0] * n
        while len(people) > 0:
            p = people.pop()
            h, k = p
            k += 1
            for i in range(n):
                if ret[i] == 0 or ret[i][0] >= h:
                    k -= 1
                if k == 0:
                    break
            ret[i] = p
        return ret