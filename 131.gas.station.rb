# @param {Integer[]} gas
# @param {Integer[]} cost
# @return {Integer}
def can_complete_circuit(gas, cost)
    start = gas.length - 1
    pos = 0
    left = gas[start] - cost[start]
    while start > pos
        if left >= 0
            left += gas[pos] - cost[pos]
            pos += 1 
        else
            start -= 1
            left += gas[start] - cost[start]
        end
    end
    return left >= 0 ? start : -1
end