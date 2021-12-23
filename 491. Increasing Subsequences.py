class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seqs = set()
        n = len(nums)
        def find(i, seq):
            if i == n:
                return
            find(i+1, seq)
            if len(seq) == 0 or seq[-1] <= nums[i]:
                seq.append(nums[i])
                if len(seq) > 1:
                    seqs.add(tuple(seq))
                find(i+1, seq)
                seq.pop()
        find(0, [])
        return list(seqs)