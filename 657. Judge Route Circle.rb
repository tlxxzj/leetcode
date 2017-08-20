# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
    u,d,l,r=0,0,0,0
    moves.each_char do |m|
        case m
            when 'U' then u+=1
            when 'D' then d+=1
            when 'L' then l+=1
            else          r+=1
        end
    end
    u==d && l==r
end