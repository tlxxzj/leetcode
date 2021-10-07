class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        popped.reverse()
        stack = []
        for i in pushed:
            stack.append(i)
            while len(stack) > 0 and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return len(stack) == 0
        