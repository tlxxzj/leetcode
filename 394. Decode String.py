class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        q = []
        i = 0
        while i < n:
            if s[i].isdigit():
                j = i + 1
                while s[j].isdigit():
                    j += 1
                q.append(int(s[i:j]))
                i = j
            elif s[i] == '[':
                q.append('[')
                i += 1
            elif s[i] == ']':
                i += 1
                x = ''
                while q[-1] != '[':
                    x = q.pop() + x
                q.pop()
                x = q.pop() * x
                q.append(x)
            else:
                j = i + 1
                while j < n and s[j].isalpha():
                    j += 1
                q.append(s[i:j])
                i = j
        #print(q)
        return ''.join(q)
            