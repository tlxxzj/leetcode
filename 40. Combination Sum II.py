class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        q = [(0, 0, [])]
        ret = []
        while len(q) > 0:
            i, s, nums = q.pop()
            #print(i, s, nums)
            if s == target:
                ret.append(nums)
                continue
            if i >= n or s + candidates[i] > target:
                continue
            k = i + 1
            while k < n and candidates[i] == candidates[k]:
                k += 1
            q.append((k, s, nums))
            j = i + 1
            while j <= k:
                if s + candidates[i] * (j-i) <= target:
                    q.append((k, s + candidates[i] * (j-i), nums+[candidates[i]]*(j-i)))
                else:
                    break
                j += 1
        return ret
