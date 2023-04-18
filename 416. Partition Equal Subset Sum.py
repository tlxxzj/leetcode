class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if n < 2 or total_sum & 1 == 1:
            return False
        
        target = total_sum // 2
        subsets = set([0])
        for num in nums:
            new_subsets = []
            for sub in subsets:
                new_sub = sub + num
                if new_sub == target:
                    return True
                if new_sub not in subsets and new_sub < target:
                    new_subsets.append(new_sub)
            subsets.update(new_subsets)
        return False
            
