# @param {Integer} n
# @return {Integer}
def integer_break(n)
    dp = Array.new(n+1, 1)
    for i in 3..n
        for j in 1..i-1
            x = [j, dp[j]].max
            y = [i-j, dp[i-j]].max
            z = x * y
            dp[i] = z if z > dp[i]
        end
    end
    dp[n]
end

