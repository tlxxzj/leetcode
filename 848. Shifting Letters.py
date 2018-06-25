class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        def shift(c, x):
            return chr(((ord(c) - ord('a') + x) % 26) + ord('a'))
            
        s = list(S)
        n = len(shifts)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i + 1]
        for i in range(n):
            s[i] = shift(s[i],shifts[i])
        return ''.join(s)
        