# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
    lo, hi = 0, nums.length-1
    while lo < hi
        mid = (lo + hi) >> 1
        if nums[mid] >= nums[hi]
            lo = mid + 1
        else
            hi = mid
        end
    end
    return nums[lo]
end