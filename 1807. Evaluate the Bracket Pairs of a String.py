class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = dict(knowledge)
        ret = []
        start = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                start = i + 1
                while s[i] != ')':
                    i += 1
                ret.append(knowledge.get(s[start:i], '?'))
            else:
                ret.append(s[i])
            i += 1
        return ''.join(ret)