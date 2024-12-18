class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        preNum = nums[0]
        seq = []
        seq2 = []
        i = 0
        while i < n:
            if preNum + 1 < nums[i]:
                if seq[-1] < 3:
                    return False
                seq = []
            
            preNum = nums[i]
            j = i
            i += 1
            while i < n and nums[i-1] == nums[i]:
                i += 1
            
            for _ in range(j, i):
                if len(seq) > 0:
                    x = seq.pop()
                else:
                    x = 0
                seq2.append(x + 1)
            
            for x in seq:
                if x < 3:
                    return False
            seq = []
            seq, seq2 = seq2, seq
            seq.sort(reverse=True)
        
        return seq[-1] >= 3

