class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        popped.reverse()
        for e in pushed:
            stack.append(e)
            while len(stack) > 0 and popped[-1] == stack[-1]:
                stack.pop()
                popped.pop()
        return len(stack) == 0
        
        