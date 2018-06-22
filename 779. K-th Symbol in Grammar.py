class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        x = 0
        K -= 1
        while K > 0:
            x = x ^ 1
            K = K & (K - 1)
        return x
        
            
        