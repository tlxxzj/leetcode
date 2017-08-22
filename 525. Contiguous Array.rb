# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)
    h = {}
    diff=0
    n = nums.length
    ret=0
    for i in 0...n
        if nums[i]==0
            diff -=1
        else
            diff += 1
        end
        if h[diff].nil?
            h[diff] = [i]
        else
            h[diff] << i
        end
    end
    if h.include? 0
        ret=h[0][-1]+1
    end
    h.each do |k, v|
        if v != nil && v.length > 1 && v[-1]-v[0] > ret
            ret=v[-1]-v[0]
        end
    end
    ret
end