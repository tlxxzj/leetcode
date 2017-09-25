class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            h = ''.join(sorted(s))
            if h in d:
                d[h].append(s)
            else:
                d[h] = [s]
        return list(d.values())
        