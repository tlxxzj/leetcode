# @param {Integer} n
# @return {String}
def convert_to_title(n)
    return n>0 ? (convert_to_title((n-1)/26) + ((n-1)%26+65).chr) : '' 
end
