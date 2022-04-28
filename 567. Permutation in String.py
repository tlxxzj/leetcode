class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        l1, l2 = len(s1), len(s2)
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        
        i = 0
        while i < l2:
            j = i
            while i < l2:
                if s2[i] in d1:
                    if d1[s2[i]] > 0:
                        d1[s2[i]] -= 1
                        if i - j + 1 == l1:
                            return True
                    else:
                        while s2[j] != s2[i]:
                            d1[s2[j]] += 1  
                            j += 1
                        j += 1
                    i += 1
                else:
                    while j < i:
                        if s2[j] in d1:
                            d1[s2[j]] += 1
                        j += 1
                    break
            i += 1
        return False