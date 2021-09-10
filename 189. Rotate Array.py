class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gcd(a, b):
            if a % b == 0:
                return b
            else:
                return gcd(b, a%b)

        n = len(nums)
        k = k % n
        if k == 0:
            return
        g = gcd(n, k)
        l = n * k / g / k
        j = 0
        x = nums[0]
        for i in range(n):
            #print(x, nums)
            jk = (j + k)%n
            y = nums[jk]
            nums[jk] = x
            x = y
            if g != 1 and (i+1) % l == 0:
                j = (j + k + 1) % n
                x = nums[j]
            else:
                j = jk