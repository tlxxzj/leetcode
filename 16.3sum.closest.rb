# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
    ret = nums[0] + nums[1] + nums[2]
    nums.sort!
    for i in 0..nums.length-1
        l, r = i + 1, nums.length-1
        while l < r
            sum = nums[i] + nums[l] + nums[r]
            if sum != target
                if (sum-target).abs < (ret-target).abs
                    ret = sum
                end
                if sum < target then l += 1 else r -= 1 end
            else
                return target
            end
        end
    end
    return ret
end