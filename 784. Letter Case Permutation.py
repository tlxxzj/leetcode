class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = [s]
        s = list(s)
        n = len(s)
        
        def get_permutation(i):
            if i == n:
                return
            c = s[i]
            if 'a' <= s[i] <= 'z':
                s[i] = chr(ord(s[i]) - 32)
                ret.append(''.join(s))
                get_permutation(i+1)
            elif 'A' <= s[i] <= 'Z':
                s[i] = chr(ord(s[i]) + 32)
                ret.append(''.join(s))
                get_permutation(i+1)
            s[i] = c
            get_permutation(i+1)
        
        get_permutation(0)
        return ret
            