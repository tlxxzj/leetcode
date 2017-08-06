class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        l1, l2 = len(v1), len(v2)
        i = 0
        ml = max(l1, l2)
        x,y=0,0
        while i < ml:
            x=v1[i] if i<l1 else 0
            y=v2[i] if i<l2 else 0
            if x < y:
                return -1
            elif x > y:
                return 1
            i += 1
        return 0
