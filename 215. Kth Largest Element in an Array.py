class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def kth(l, r):
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            p = nums[l]
            i, j = l, r
            while i < j:
                while i < r and nums[i] <= p:
                    i += 1
                while j > l and nums[j] > p:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                else:
                    break
            if i > j:
                i, j = j, i
            nums[l] = nums[i]
            nums[i] = p
            #print(nums, i, j, p)
            if n - k == i:
                return nums[i]
            if n - k < i:
                return kth(l, i-1)
            else:
                return kth(i+1, r)
        return kth(0, n-1)