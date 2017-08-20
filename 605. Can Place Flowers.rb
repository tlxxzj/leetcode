# @param {Integer[]} flowerbed
# @param {Integer} n
# @return {Boolean}
def can_place_flowers(flowerbed, n)
    cnt = 0
    len = flowerbed.length
    i = 0
    k = 0
    while i < len
        if flowerbed[i]==1 
            i += 1
            next
        end
        while i+k < len && flowerbed[i+k] == 0
            k += 1
        end
        x = k - 2 + 1
        if i==0
            x += 1 
        end
        if i+k==len
            x += 1
        end
        if x >0
            cnt += x/2
        end
        i+=k
        k=0
    end
    cnt >= n
end

