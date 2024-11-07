func kthSmallest(matrix [][]int, k int) int {
    n := len(matrix)
    l, r := matrix[0][0], matrix[n-1][n-1]
    
    for l < r {
        m := l + (r - l) / 2

        num := 0
        x, y := 0, n-1
        for x < n && y >= 0 {
            for y >= 0 && matrix[x][y] > m {
                y--
            }
            x++
            num += y + 1
        }
        if num >= k {
            r = m
        } else {
            l = m + 1
        }
    }

    return l
}
