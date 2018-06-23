class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        key_map = {}
        for i, c in enumerate(S):
            key_map[c] = i
        T = list(T)
        T.sort(key=lambda x: key_map.get(x, 26))
        return ''.join(T)
        