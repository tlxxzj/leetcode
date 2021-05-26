class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(l: list, start: int, end: int):
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
        
        letters = []
        bracket_positions = []
        for c in s:
            if c == '(':
                bracket_positions.append(len(letters))
            elif c == ')':
                reverse(letters, bracket_positions.pop(), len(letters)-1)
            else:
                letters.append(c)
        return ''.join(letters)