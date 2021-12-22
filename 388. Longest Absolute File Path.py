class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        maxPathLen = 0
        dirs = []
        for line in lines:
            t = line.count('\t')
            # file
            if '.' in line:
                if t == 0:
                    maxPathLen = max(maxPathLen, len(line))
                else:
                    path = dirs[t-1] + '/' + line[t:]
                    #print(path)
                    maxPathLen = max(maxPathLen, len(path))
            # dir
            else:
                if t == len(dirs):
                    dirs.append('')
                if t == 0:
                    dirs[0] = line
                else:
                    dirs[t] = dirs[t-1] + '/' + line[t:]
            #print(dirs)
        return maxPathLen
