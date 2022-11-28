class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums2 = {}
        for num in nums:
            if num in nums2:
                nums2[num] += 1
            else:
                nums2[num] = 1
        
        ans = [[]]
        for k, v in nums2.items():
            ans2 = []
            for arr in ans:
                for i in range(1, v+1):
                    ans2.append(arr + [k] * i)
            ans.extend(ans2)
        
        return ans

