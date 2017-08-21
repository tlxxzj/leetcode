# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def set_zeroes(matrix)
    m = matrix.length
    n = matrix[0].length
    row, col = false, false
    for i in 0...m
        for j in 0...n
            if matrix[i][j] == 0
                matrix[i][0] = 0
                matrix[0][j] = 0
                if i==0 then row=true end
                if j==0 then col=true end
            end
        end
    end
    for i in 1...m
        for j in 1...n
            matrix[i][j] = 0 if matrix[i][0]==0 || matrix[0][j]==0
        end
    end
    if row
        for j in 0...n
            matrix[0][j]=0
        end
    end
    if col
        for i in 0...m
            matrix[i][0]=0
        end
    end
end