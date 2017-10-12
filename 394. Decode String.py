class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = [0, len(s)]
        def next_token():
            if st[0] >= st[1]:
                return ['eof', 0]
            elif s[st[0]].isdigit():
                begin = st[0]
                while st[0] < st[1] and s[st[0]].isdigit():
                    st[0] += 1
                return ['int', int(s[begin: st[0]])]
            elif s[st[0]].isalpha():
                begin = st[0]
                while st[0] < st[1] and s[st[0]].isalpha():
                    st[0] += 1
                return ['str', s[begin: st[0]]]
            else:
                st[0] += 1
                return ['[]', 0]
        '''
        while 1:
            tok = next_token()
            print tok
            if tok[0] == 'eof':
                break
        '''
        
        def decode(e):
            tok = next_token()
            r = ''
            while tok[0] != e:
                if tok[0] == 'int':
                    t = tok[1]
                    next_token() # '['
                    s = decode('[]')
                    r += s*t
                elif tok[0] =='str':
                    r += tok[1]
                tok = next_token()
            return r
        
        return decode('eof')
                
            
            
        