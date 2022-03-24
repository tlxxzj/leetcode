class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def nextPermutation(ns):
            i = len(ns)-1
            while i-1 >= 0 and ns[i-1] >= ns[i]:
                i -= 1
            if i == 0:
                return None
            j = len(ns)-1
            while ns[j] <= ns[i-1]:
                j -= 1
            ns[i-1], ns[j] = ns[j], ns[i-1]
            j = len(ns)-1
            while i < j:
                ns[i], ns[j] = ns[j], ns[i]
                i += 1
                j -= 1
            return ns
        
        nums.sort()
        ret = [nums[:]]
        while True:
            x = nextPermutation(nums)
            if not x:
                break
            ret.append(x[:])
        return ret
            