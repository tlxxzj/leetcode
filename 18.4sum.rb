# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def four_sum(nums, target)
    ret = []
    nums.sort!
    for i in 0..nums.length-4
        if i > 0 and nums[i] == nums[i-1] then next end
        for j in i+1..nums.length-3
            if j > i+1 and nums[j] == nums[j-1] then next end
            l, r = j + 1, nums.length - 1
            while l < r
                sum = nums[i] + nums[j] + nums[l] + nums[r]
                if sum < target
                    l += 1
                elsif sum > target
                    r -= 1
                else
                    ret << [nums[i], nums[j], nums[l], nums[r]]
                    while l < r and nums[l] == nums[l + 1] do l += 1 end
                    while l < r and nums[r] == nums[r - 1] do r -= 1 end
                    l += 1; r -= 1
                end
            end
        end
    end
    return ret
end

