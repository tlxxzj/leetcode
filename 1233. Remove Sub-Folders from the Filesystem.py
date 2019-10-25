class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        ret = [folder[0]]
        root = ret[0]
        for f in folder[1:]:
            if f.startswith(root) and f[len(root)] == '/':
                continue
            else:
                ret.append(f)
                root = f
        return ret