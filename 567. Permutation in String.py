class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        if len1 >len2:
            return False
        
        def c2i(c):
            return ord(c)-ord('a')
        
        cnt = [0]*26
        bl = 0
        for c in s1:
            cnt[c2i(c)] +=1 
            if cnt[c2i(c)] == 1:
                bl += 1
        
        for c in s2[:len1-1]:
            cnt[c2i(c)] -= 1
            if cnt[c2i(c)] == 0:
                bl -= 1
            elif cnt[c2i(c)] == -1:
                bl += 1
        
        for i in range(len1-1, len2):
            c = s2[i]
            cnt[c2i(c)] -= 1
            if cnt[c2i(c)] == 0:
                bl -= 1
            elif cnt[c2i(c)] == -1:
                bl += 1
            
            if bl == 0:
                return True
            
            
            c = s2[i-len1+1]
            cnt[c2i(c)] += 1
            if cnt[c2i(c)]==0:
                bl -= 1
            elif cnt[c2i(c)] == 1:
                bl +=1
                
        return False
        
        