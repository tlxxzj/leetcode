class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        for tok in tokens:
            #print(q)
            if tok == '+':
                q.append(q.pop() + q.pop())
            elif tok == '-':
                b, a = q.pop(), q.pop()
                q.append(a - b)
            elif tok == '*':
                q.append(q.pop() * q.pop())
            elif tok == '/':
                b, a = q.pop(), q.pop()
                q.append(int(a/b))
            else:
                q.append(int(tok))
        return q[0]