class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a, b = 0, 0
        n = len(secret)
        h = {}
        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                h[secret[i]] = h.get(secret[i], 0) + 1
        
        for i in range(n):
            if secret[i] != guess[i]:
                if h.get(guess[i], 0) > 0:
                    b += 1
                    h[guess[i]] -= 1
        
        return str(a)+'A'+str(b)+'B'
        
        