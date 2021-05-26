class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        new_dirs = []
        for d in dirs:
            if d == '' or d == '.':
                continue
            if d == '..':
                if len(new_dirs) > 0:
                    new_dirs.pop()
            else:
                new_dirs.append(d)
        return '/' + '/'.join(new_dirs)
