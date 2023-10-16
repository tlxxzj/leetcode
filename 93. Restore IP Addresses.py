class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ips = []
        ip = [0,1,2,3]

        def restore(i, j, k):
            if k>=4 or j>n or int(s[i:j])>255 or (j-i>1 and s[i]=="0"):
                return
            
            ip[k] = s[i:j]
            if j == n and k == 3:
                ips.append(".".join(ip))
            else:
                restore(j, j+1, k+1)
                restore(j, j+2, k+1)
                restore(j, j+3, k+1)

        restore(0, 1, 0)
        restore(0, 2, 0)
        restore(0, 3, 0)

        return ips
