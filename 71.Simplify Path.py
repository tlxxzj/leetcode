class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = []
        for i in path.split('/'):
            if i == '' or i == '.': continue
            if i == '..':
                if len(ret)>0: ret.pop()
            else:
                ret.append(i)
        return '/' + '/'.join(ret)
        