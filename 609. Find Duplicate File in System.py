class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        import re
        p = re.compile('^([^\(]+)\(([^\)]+)\)$')
        
        same = {}
        for d in paths:
            fs = d.split(' ')
            root = fs[0]
            for f in fs[1:]:
                m = p.match(f)
                filename = root + '/' + m[1]
                content = m[2]
                if content not in same:
                    same[content] = []
                same[content].append(filename)
        
        return list(filter(lambda x: len(x)>1, same.values()))