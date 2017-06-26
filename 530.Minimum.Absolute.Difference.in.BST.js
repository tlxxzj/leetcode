/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var getMinimumDifference = function(root) {
    function cmp(a, b){
        return a-b;
    }
    function travel(node, list){
        if (node === null) return;
        list.push(node.val);
        travel(node.left, list);
        travel(node.right, list);
    }
    list = [];
    travel(root, list);
    list = list.sort(cmp);
    ret = list[1] - list[0];
    for(var i = 2; i < list.length; ++i)
    {
        if (list[i] - list[i-1] < ret)
        {
            ret = list[i] - list[i-1];
        }
    }
    return ret;
};