# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} t1
# @param {TreeNode} t2
# @return {TreeNode}
def merge_trees(t1, t2)
    if t1 == nil and t2 == nil then return nil end
    val1, val2, l1, l2, r1, r2 = 0, 0, nil, nil, nil, nil
    if t1 != nil
        val1 = t1.val
        l1 = t1.left
        r1 = t1.right
    end
    if t2 != nil
        val2 = t2.val
        l2 = t2.left
        r2 = t2.right
    end
    root = TreeNode.new(val1 + val2)
    root.left = merge_trees(l1, l2)
    root.right = merge_trees(r1, r2)
    return root
end