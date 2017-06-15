# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
    ret = []
    nums.sort!
    for i in 0..nums.length-1
        if i > 0 and nums[i] == nums[i-1] then next end
        l, r = i+1, nums.length-1
        while l < r
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0 then l += 1
            elsif sum > 0 then r -= 1
            else
                ret << [nums[i], nums[l], nums[r]]
                while l < r and nums[l] == nums[l + 1] do l += 1 end
                while l < r and nums[r] == nums[r - 1] do r -= 1 end
                l += 1
                r -= 1
            end
        end
    end
    return ret
end


