# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} s
# @param {TreeNode} t
# @return {Boolean}
def is_subtree(s, t)
    def is_sub(s, t)
        if s==nil and t==nil then return true end
        if s==nil or t == nil or s.val != t.val then return false end
        if !is_sub(s.left, t.left) then return false end
        if !is_sub(s.right, t.right) then return false end
        return true
    end
    if is_sub(s, t) then return true end
    if s.left and is_subtree(s.left, t) then return true end
    if s.right and is_subtree(s.right, t) then return true end
    return false
end