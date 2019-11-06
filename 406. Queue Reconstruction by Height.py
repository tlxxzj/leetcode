from functools import cmp_to_key
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        ret = [0] * n
        def cmp(a, b):
            if a[0] == b[0]:
                return a[1] - b[1]
            return a[0] - b[0]
        people.sort(key=cmp_to_key(cmp))
        #print(people)
        for p in people:
            h, k = p[0], p[1]
            x = -1
            for i in range(n):
                if ret[i] == 0 or ret[i][0] >= h:
                    x += 1
                if ret[i] == 0 and x == k:
                    ret[i] = p
                    break
                
        return ret
        