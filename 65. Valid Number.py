class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def test_frac(s):
            if not s:
                return True
            n = len(s)
            i=0
            if s[i].isdigit():
                while i < n and s[i].isdigit():
                    i += 1
                if i==n:
                    return True
                if s[i]=='e':
                    return test_exp(s[i+1:])
            elif s[i].lower()=='e':
                return test_exp(s[i+1:])
            return s[i:].isspace()

        def test_exp(s):
            if not s:
                return False
            n=len(s)
            i=0
            if i < n and s[i] in ['-', '+']:
                i += 1
            if i == n or not s[i].isdigit():
                return False
            while i <n and s[i].isdigit():
                i += 1
            return i==n or s[i:].isspace()

        s = str(s)
        n = len(s)
        i = 0
        #skip lead white space
        while i < n and s[i].isspace():
            i += 1
        
        if i < n and s[i]  in ['-', '+']:
            i += 1

        if i < n and s[i].isdigit():
            while i < n and s[i].isdigit():
                i +=1
            if i < n and s[i].lower() == 'e':
                return test_exp(s[i+1:])
            elif i < n and s[i] == '.':
                return test_frac(s[i+1:])
            else:
                return i==n or s[i:].isspace()
        elif i < n and s[i] == '.':
            i+=1
            if i<n and s[i].isdigit():
                return test_frac(s[i:])

        return False
