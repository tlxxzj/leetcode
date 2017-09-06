class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def merge_sort(l, r):
            if l>=r:
                return 0
            ret = 0
            m = (l+r)/2
            lr = merge_sort(l, m)
            rr = merge_sort(m+1, r)
            #print nums[l:m+1], nums[m+1:r+1]
            i, j, k, st = l, m+1, l, []
            while i <= m and j <= r:
                if nums[i] < nums[j]:
                    st.append(nums[i])
                    i += 1
                else:
                    while k <= m and nums[k] <= 2 * nums[j]:
                        k += 1
                    ret+= m-k+1
                    st.append(nums[j]) 
                    j += 1
            while i <=m:
                st.append(nums[i])
                i += 1
            while j <= r:
                while k <= m and nums[k] <= 2 * nums[j]:
                    k += 1
                ret+= m-k+1
                st.append(nums[j])
                j += 1
            nums[l:r+1] = st
            return ret + lr + rr

        return merge_sort(0, n-1)

#S = Solution()

#print S.reversePairs([-5, -5])