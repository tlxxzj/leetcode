# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        seg = [0] * 4 * (n+1)
        def seg_init(k, l, r):
            if l==r:
                seg[k]=l
            else:
                m=(l+r)/2
                seg_init(k<<1, l, m)
                seg_init(k<<1|1, m+1, r)
                if nums[seg[k<<1]] > nums[seg[k<<1|1]]:
                    seg[k] = seg[k<<1]
                else:
                    seg[k] = seg[k<<1|1]
        
        def seg_query(k, L, R, l, r):
            if l >=L and r <= R:
                return seg[k]
            m = (l+r)/2
            ret=None
            if m>=L:
                x = seg_query(k<<1, L, R, l, m)
                if ret is None or nums[x] > nums[ret]:
                    ret = x
            if m+1<=R:
                x = seg_query(k<<1|1, L, R, m+1, r)
                if ret is None or nums[x] > nums[ret]:
                    ret=x
            return ret
        
        def to_tree(l, r):
            if l >r: return None
            x = seg_query(1, l, r, 0, n-1)
            if x <l or x > r:
                print 'error----------------------------'
                exit(0)
            node = TreeNode(nums[x])
            node.left = to_tree(l, x-1)
            node.right = to_tree(x+1, r)
            return node
            
        
        if n>0:
            seg_init(1, 0, n-1)
        return to_tree(0, n-1)
        

#S = Solution()
#S.constructMaximumBinaryTree([3,2,1,6,0,5])
