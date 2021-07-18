class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        all_files = defaultdict(list)
        for path in paths:
            files = path.split(' ')
            root = files[0]
            for file in files[1:]:
                lp_index = file.index('(')
                filename, content = file[:lp_index], file[lp_index+1:-1]
                full_path = f'{root}/{filename}'
                all_files[content].append(full_path)
        
        return list(filter(lambda x:len(x) > 1, all_files.values()))