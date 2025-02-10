class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = float('-inf')
        s = []
        for num in nums[::-1]:
            if num < k:
                return True
            while len(s) > 0 and s[-1] < num:
                k = max(k, s.pop())
            s.append(num)
        
        return False
