class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for c in s:
            if c in ['[', '{', '(']:
                q.append(c)
            elif c == ']':
                if len(q) == 0 or q.pop() != '[':
                    return False
            elif c == '}':
                if len(q) == 0 or q.pop() != '{':
                    return False
            elif c == ')':
                if len(q) == 0 or q.pop() != '(':
                    return False
            else:
                return False
        return len(q) == 0