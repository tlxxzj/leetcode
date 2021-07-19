class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ret = 0
        n = len(arr)
        up, down = 0, 0
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                down = 0
                up += 1
            elif arr[i] < arr[i-1]:
                down += 1
                if up > 0:
                    ret = max(ret, up + down + 1)
                    if i+1 < n and arr[i] <= arr[i+1]:
                        up, down = 0,0
            else:
                up, down = 0, 0
        return ret

            