# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
    str = str.split(' ')
    h1 = {}
    h2 = {}
    return false if pattern.length != str.length
    for i in 0...str.length
        p =pattern[i]
        s = str[i]
        if h1[p].nil? && h2[s].nil? 
            h1[p] = s
            h2[s]=p
        elsif h1[p] == s && h2[s] == p
            next
        else
            return false
        end
    end
    true
end