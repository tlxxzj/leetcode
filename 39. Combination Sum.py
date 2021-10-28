class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        q = [(0, 0, [])]
        while len(q) > 0:
            i, s, nums = q.pop()
            if s == target:
                ret.append(nums)
                continue
            if i >= len(candidates) or s + candidates[i] > target:
                continue
            q.append((i, s + candidates[i], nums+[candidates[i]]))
            q.append((i+1, s, nums))
        return ret