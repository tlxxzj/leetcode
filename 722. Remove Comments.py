class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        ret = []
        code = '\n'.join(source)
        n = len(code)
        i = 0
        while i < n:
            if i+1 < n and code[i] == '/' and code[i+1] == '/':
                i += 2
                while i < n and code[i] != '\n':
                    i += 1
            elif i+1 < n and code[i] == '/' and code[i+1] == '*':
                i += 2
                while i+1 < n and not (code[i] == '*' and code[i+1] == '/'):
                    i += 1
                i += 2
            else:
                ret.append(code[i])
                i += 1

        ret = ''.join(ret)
        print(ret)
        ret = ret.split('\n')
        ret2 = []
        for line in ret:
            if line != '' and line != '\n' :
                ret2.append(line)
        return ret2