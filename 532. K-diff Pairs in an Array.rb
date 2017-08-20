# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_pairs(nums, k)
    return 0 if k < 0
    h = Hash.new(0)
    ret = 0
    nums.each do |i| h[i] += 1 end
    h.each do |x,y|
        if k == 0
            if y > 1 then ret += 1 end
        else
            if h[x+k] > 0 then ret += 1 end
        end
    end
    return ret
end

puts find_pairs([1,2,3,4,5], -1)