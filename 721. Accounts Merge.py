class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        f = {}
        groups = {}
        names = {}

        def getf(email):
            while email != f.get(email, email):
                email = f[email]
            return email
        
        for account in accounts:
            name = account[0]
            root = getf(account[1])
            for email in account[1:]:
                f[getf(email)] = root
                names[email] = name
            
        for email in f.keys():
            group = getf(email)
            if group not in groups:
                groups[group] = [names[group]]
            groups[group].append(email)
        
        ret = []
        for group in groups.values():
            ret.append([group[0]] + sorted(group[1:]))
        
        return ret
        

            
