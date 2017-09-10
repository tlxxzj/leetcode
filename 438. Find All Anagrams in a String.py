class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        oa = ord('a')
        def c2x(c):
            return ord(c)-oa
        
        sl = len(s)
        pl = len(p)
        st = [0] * 26
        for c in p:
            st[c2x(c)] += 1
        
        nz = 0
        for i in st:
            if i:
                nz += 1
        
        for c in s[:pl-1]:
            x=c2x(c)
            if st[x] ==0:
                st[x] -= 1
                nz += 1
            else:
                st[x] -= 1
                if st[x] == 0:
                    nz -= 1
        ret = []
        i = pl-1
        for i in range(pl-1, sl):
            c = s[i]
            x=c2x(c)
            if st[x] == 0:
                st[x] -= 1
                nz +=1
            else:
                st[x] -= 1
                if st[x] ==0:
                    nz -= 1
            if nz ==0 :
                ret.append(i-pl+1)
            
            x = c2x(s[i-pl+1])
            if st[x] == 0:
                st[x] += 1
                nz += 1
            else:
                st[x] += 1
                if st[x] == 0:
                    nz -= 1
        
        return ret
        