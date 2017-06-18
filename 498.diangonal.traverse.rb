# @param {Integer[][]} matrix
# @return {Integer[]}
def find_diagonal_order(matrix)
    if matrix == nil or matrix.length == 0 then return [] end
    ret = []
    m = matrix.length
    n = matrix[0].length
    i, j, up = 0, 0, false
    while true
        up = !up
        if up
            while i >= 0 and j < n
                ret << matrix[i][j]
                i -= 1; j += 1
            end
            i += 1; j -= 1
            if j < n - 1
                j += 1
            elsif i < m - 1
                i += 1
            else
                break
            end
        else
            while i < m and j >= 0
                ret << matrix[i][j]
                i += 1; j -= 1
            end
            i -= 1; j += 1;
            if i < m - 1
                i += 1
            elsif j < n - 1
                j += 1
            else
                break
            end
        end
    end
    return ret
end