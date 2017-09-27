class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        n = len(data)
        while i < n:
            if data[i] & 0xf8 == 0xf0:
                j = 3
            elif data[i] & 0xf0 == 0xe0:
                j = 2
            elif data[i] & 0xe0 == 0xc0:
                j = 1
            elif data[i] & 0x80 == 0:
                j = 0
            else:
                return False
            print 'i, j = ', i, j
            for k in xrange(j):
                i += 1
                if i >= n:
                    return False
                if data[i] & 0xc0 != 0x80:
                    return False
            i += 1
            print 'i = ', i
                
                
                
        
        return i == n
        
        