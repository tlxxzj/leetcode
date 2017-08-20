# @param {Integer[]} nums
# @return {Integer}
def find_unsorted_subarray(nums)
    nums2 = nums.sort
    n = nums.length
    i, j = 0, n-1
    while i < n && nums[i] == nums2[i] then i+=1 end
    while j > i && nums[j] == nums2[j] then j-=1 end
    j-i+1
end