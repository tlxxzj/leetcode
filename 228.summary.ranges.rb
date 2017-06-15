# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
    def range2str(start, finish)
        return start == finish ? (start.to_s) : ("#{start}->#{finish}")
    end
    ret = []
    start = nil
    finish = nil
    for i in nums
        if start == nil
            start = i
            finish = i
        elsif finish + 1 == i
            finish = i
        else
            ret << range2str(start, finish)
            start = i
            finish = i
        end
    end
    if start != nil
        ret << range2str(start, finish)
    end
    return ret
end
