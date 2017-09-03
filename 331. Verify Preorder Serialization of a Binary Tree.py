class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False
        pre = preorder.split(',')
        n = len(pre)
        i = 0
        ret = [True]
        def valid(i):
            if i >= n:
                ret[0] = False
            elif pre[i] != '#':
                l = valid(i+1)
                r = valid(l+1)
                return r        
            return i

        if valid(0) != n-1:
            ret[0] = False
        return ret[0]

