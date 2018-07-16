class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        def find(f, x):
            if x not in f:
                f[x] = x
                return x
            elif x == f[x]:
                return x
            else:
                y = find(f, f[x])
                f[x] = y
                return y


        def join(f, x, y):
            x1 = find(f, x)
            y1 = find(f, y)
            f[x1] = y1

        f = {}
        name = {}
        for account in accounts:
            for e in account[1:]:
                join(f, account[1], e)
                name[e] = account[0]

        accs = {}
        for e in f.keys():
            ef = find(f, e)
            if ef not in accs:
                accs[ef] = [e]
            else:
                accs[ef].append(e)

        for k, v in accs.items():
            v.sort()

        return [[name[v[0]]] + v for k, v in accs.items()]