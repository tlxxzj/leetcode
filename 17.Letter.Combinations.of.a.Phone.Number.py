class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        char = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ret = ['']
        for d in digits:
            d = int(d)
            add = [s+c for s in ret for c in char[d]]
            ret = add
        if ret[0] == '': return []
        else: return ret